#define _DARWIN_C_SOURCE
#define _DEFAULT_SOURCE
#define _POSIX_C_SOURCE 200809L

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>
#include <unistd.h>

typedef struct {
    _Atomic uint64_t value;
} adjacent_counter;

typedef struct {
    _Atomic uint64_t value;
    unsigned char padding[120];
} padded_counter;

typedef struct {
    uint64_t iterations;
    size_t index;
    int mode;
    pthread_mutex_t *lock;
    uint64_t *shared;
    adjacent_counter *adjacent;
    padded_counter *padded;
    uint64_t local;
} worker_args;

static struct rusage usage_before;

static void begin_measurement(void) {
    if (getrusage(RUSAGE_SELF, &usage_before) != 0) {
        perror("getrusage");
        exit(2);
    }
}

static uint64_t timeval_ns(struct timeval value) {
    return (uint64_t)value.tv_sec * UINT64_C(1000000000) +
           (uint64_t)value.tv_usec * UINT64_C(1000);
}

static uint64_t monotonic_ns(void) {
    struct timespec value;
    if (clock_gettime(CLOCK_MONOTONIC, &value) != 0) {
        perror("clock_gettime");
        exit(2);
    }
    return (uint64_t)value.tv_sec * UINT64_C(1000000000) + (uint64_t)value.tv_nsec;
}

static uint64_t parse_u64(const char *text, const char *name, uint64_t lower, uint64_t upper) {
    char *end = NULL;
    errno = 0;
    unsigned long long value = strtoull(text, &end, 10);
    if (errno != 0 || end == text || *end != '\0' || value < lower || value > upper) {
        fprintf(stderr, "invalid %s: %s\n", name, text);
        exit(2);
    }
    return (uint64_t)value;
}

static void emit(const char *probe, const char *variant, uint64_t operations,
                 uint64_t bytes, uint64_t checksum, uint64_t elapsed_ns,
                 const char *outcome) {
    struct rusage usage_after;
    if (getrusage(RUSAGE_SELF, &usage_after) != 0) {
        perror("getrusage");
        exit(2);
    }
    uint64_t rss = (uint64_t)usage_after.ru_maxrss;
#ifndef __APPLE__
    rss *= UINT64_C(1024);
#endif
    printf("{\"probe\":\"%s\",\"variant\":\"%s\",\"operations\":%" PRIu64
           ",\"bytes\":%" PRIu64 ",\"checksum\":%" PRIu64
           ",\"elapsed_ns\":%" PRIu64 ",\"user_cpu_ns\":%" PRIu64
           ",\"system_cpu_ns\":%" PRIu64 ",\"max_rss_bytes\":%" PRIu64
           ",\"minor_faults\":%ld,\"major_faults\":%ld"
           ",\"voluntary_context_switches\":%ld,\"involuntary_context_switches\":%ld"
           ",\"block_inputs\":%ld,\"block_outputs\":%ld,\"outcome\":\"%s\"}\n",
           probe, variant, operations, bytes, checksum, elapsed_ns,
           timeval_ns(usage_after.ru_utime) - timeval_ns(usage_before.ru_utime),
           timeval_ns(usage_after.ru_stime) - timeval_ns(usage_before.ru_stime), rss,
           usage_after.ru_minflt - usage_before.ru_minflt,
           usage_after.ru_majflt - usage_before.ru_majflt,
           usage_after.ru_nvcsw - usage_before.ru_nvcsw,
           usage_after.ru_nivcsw - usage_before.ru_nivcsw,
           usage_after.ru_inblock - usage_before.ru_inblock,
           usage_after.ru_oublock - usage_before.ru_oublock, outcome);
}

static int run_locality(int argc, char **argv) {
    if (argc != 5) {
        fprintf(stderr, "locality requires variant elements stride\n");
        return 2;
    }
    const char *variant = argv[2];
    uint64_t elements = parse_u64(argv[3], "elements", 1024, 2000000);
    uint64_t stride = parse_u64(argv[4], "stride", 1, 128);
    uint64_t slots = elements;
    if (strcmp(variant, "strided") == 0) {
        if (elements > 2000000 / stride) {
            fprintf(stderr, "elements times stride exceeds bound\n");
            return 2;
        }
        slots = elements * stride;
    } else if (strcmp(variant, "contiguous") != 0 &&
               strcmp(variant, "branch_predictable") != 0 &&
               strcmp(variant, "branch_mixed") != 0) {
        fprintf(stderr, "unknown locality variant\n");
        return 2;
    }

    uint64_t *values = calloc((size_t)slots, sizeof(*values));
    if (values == NULL) {
        perror("calloc");
        return 3;
    }
    if (strcmp(variant, "strided") == 0) {
        for (uint64_t i = 0; i < elements; i++) values[i * stride] = i + 1;
    } else if (strncmp(variant, "branch_", 7) == 0) {
        for (uint64_t i = 0; i < elements; i++) {
            values[i] = strcmp(variant, "branch_predictable") == 0
                ? (i >= (elements + 1) / 2)
                : (i & 1U);
        }
    } else {
        for (uint64_t i = 0; i < elements; i++) values[i] = i + 1;
    }

    uint64_t checksum = 0;
    begin_measurement();
    uint64_t start = monotonic_ns();
    if (strncmp(variant, "branch_", 7) == 0) {
        for (uint64_t i = 0; i < elements; i++) checksum += values[i] ? 7U : 3U;
    } else {
        uint64_t step = strcmp(variant, "strided") == 0 ? stride : 1;
        for (uint64_t i = 0; i < elements; i++) checksum += values[i * step];
    }
    uint64_t elapsed = monotonic_ns() - start;
    emit("locality", variant, elements, elements * sizeof(uint64_t), checksum, elapsed, "ok");
    free(values);
    return 0;
}

static int run_allocation(int argc, char **argv) {
    if (argc != 5) {
        fprintf(stderr, "allocation requires variant iterations bytes_per_iteration\n");
        return 2;
    }
    const char *variant = argv[2];
    uint64_t iterations = parse_u64(argv[3], "iterations", 1, 1000000);
    uint64_t size = parse_u64(argv[4], "bytes_per_iteration", 64, 1048576);
    if (iterations > UINT64_C(536870912) / size) {
        fprintf(stderr, "allocation total exceeds 512 MiB work bound\n");
        return 2;
    }
    if (strcmp(variant, "reuse") != 0 && strcmp(variant, "per_iteration") != 0 &&
        strcmp(variant, "working_set") != 0) {
        fprintf(stderr, "unknown allocation variant\n");
        return 2;
    }
    if (strcmp(variant, "working_set") == 0) {
        uint64_t total = iterations * size;
        unsigned char *working = malloc((size_t)total);
        if (working == NULL) return 3;
        uint64_t checksum = 0;
        begin_measurement();
        uint64_t start = monotonic_ns();
        for (uint64_t offset = 0; offset < total; offset += 4096) {
            working[offset] = (unsigned char)((offset / 4096) & 0xffU);
            checksum += working[offset];
        }
        uint64_t elapsed = monotonic_ns() - start;
        emit("allocation", variant, iterations, total, checksum, elapsed, "ok");
        free(working);
        return 0;
    }
    unsigned char *reuse = NULL;
    if (strcmp(variant, "reuse") == 0) {
        reuse = malloc((size_t)size);
        if (reuse == NULL) return 3;
    }
    uint64_t checksum = 0;
    begin_measurement();
    uint64_t start = monotonic_ns();
    for (uint64_t i = 0; i < iterations; i++) {
        unsigned char *buffer = reuse != NULL ? reuse : malloc((size_t)size);
        if (buffer == NULL) {
            free(reuse);
            return 3;
        }
        for (uint64_t offset = 0; offset < size; offset += 4096) {
            buffer[offset] = (unsigned char)((i + offset) & 0xffU);
            checksum += buffer[offset];
        }
        if (reuse == NULL) free(buffer);
    }
    uint64_t elapsed = monotonic_ns() - start;
    emit("allocation", variant, iterations, iterations * size, checksum, elapsed, "ok");
    free(reuse);
    return 0;
}

static void *worker(void *opaque) {
    worker_args *args = opaque;
    volatile uint64_t local = 0;
    for (uint64_t i = 0; i < args->iterations; i++) {
        if (args->mode == 0) {
            pthread_mutex_lock(args->lock);
            (*args->shared)++;
            pthread_mutex_unlock(args->lock);
        } else if (args->mode == 1) {
            local++;
        } else if (args->mode == 2) {
            atomic_fetch_add_explicit(&args->adjacent[args->index].value, 1,
                                      memory_order_relaxed);
        } else {
            atomic_fetch_add_explicit(&args->padded[args->index].value, 1,
                                      memory_order_relaxed);
        }
    }
    args->local = local;
    return NULL;
}

static int run_contention(int argc, char **argv) {
    if (argc != 5) {
        fprintf(stderr, "contention requires variant workers iterations\n");
        return 2;
    }
    const char *variant = argv[2];
    uint64_t workers = parse_u64(argv[3], "workers", 1, 64);
    uint64_t iterations = parse_u64(argv[4], "iterations", 100, 10000000);
    int mode = -1;
    if (strcmp(variant, "shared") == 0) mode = 0;
    if (strcmp(variant, "sharded") == 0) mode = 1;
    if (strcmp(variant, "adjacent") == 0) mode = 2;
    if (strcmp(variant, "padded") == 0) mode = 3;
    if (mode < 0) {
        fprintf(stderr, "unknown contention variant\n");
        return 2;
    }

    pthread_t *threads = calloc((size_t)workers, sizeof(*threads));
    worker_args *args = calloc((size_t)workers, sizeof(*args));
    adjacent_counter *adjacent = calloc((size_t)workers, sizeof(*adjacent));
    padded_counter *padded = calloc((size_t)workers, sizeof(*padded));
    pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
    uint64_t shared = 0;
    if (threads == NULL || args == NULL || adjacent == NULL || padded == NULL) return 3;

    begin_measurement();
    uint64_t start = monotonic_ns();
    for (uint64_t i = 0; i < workers; i++) {
        args[i] = (worker_args){iterations, (size_t)i, mode, &lock, &shared,
                                adjacent, padded, 0};
        if (pthread_create(&threads[i], NULL, worker, &args[i]) != 0) return 4;
    }
    uint64_t checksum = 0;
    for (uint64_t i = 0; i < workers; i++) {
        pthread_join(threads[i], NULL);
        if (mode == 1) checksum += args[i].local;
        if (mode == 2) checksum += atomic_load_explicit(&adjacent[i].value, memory_order_relaxed);
        if (mode == 3) checksum += atomic_load_explicit(&padded[i].value, memory_order_relaxed);
    }
    if (mode == 0) checksum = shared;
    uint64_t elapsed = monotonic_ns() - start;
    emit("contention", variant, workers * iterations, 0, checksum, elapsed, "ok");
    pthread_mutex_destroy(&lock);
    free(threads); free(args); free(adjacent); free(padded);
    return checksum == workers * iterations ? 0 : 5;
}

static int write_all(int descriptor, const unsigned char *buffer, size_t size) {
    size_t offset = 0;
    while (offset < size) {
        ssize_t count = write(descriptor, buffer + offset, size - offset);
        if (count < 0 && errno == EINTR) continue;
        if (count <= 0) return -1;
        offset += (size_t)count;
    }
    return 0;
}

static int run_io(int argc, char **argv) {
    if (argc != 7) {
        fprintf(stderr, "io requires variant total_bytes chunk_bytes sync_every path\n");
        return 2;
    }
    const char *variant = argv[2];
    uint64_t total = parse_u64(argv[3], "total_bytes", 4096, 536870912);
    uint64_t chunk = parse_u64(argv[4], "chunk_bytes", 1, 1048576);
    uint64_t sync_every = parse_u64(argv[5], "sync_every", 0, 1000000);
    const char *path = argv[6];
    if (total % chunk != 0) {
        fprintf(stderr, "total_bytes must be divisible by chunk_bytes\n");
        return 2;
    }
    int descriptor = open(path, O_CREAT | O_TRUNC | O_WRONLY, 0600);
    if (descriptor < 0) { perror("open"); return 3; }
    unsigned char *buffer = malloc((size_t)chunk);
    if (buffer == NULL) return 3;
    memset(buffer, 0xa5, (size_t)chunk);
    uint64_t writes = total / chunk;
    uint64_t syncs = 0;
    uint64_t checksum = 0;
    begin_measurement();
    uint64_t start = monotonic_ns();
    for (uint64_t i = 0; i < writes; i++) {
        if (write_all(descriptor, buffer, (size_t)chunk) != 0) return 4;
        checksum += UINT64_C(0xa5) * chunk;
        if (sync_every > 0 && (i + 1) % sync_every == 0) {
            if (fsync(descriptor) != 0) return 4;
            syncs++;
        }
    }
    if (sync_every > 0 && writes % sync_every != 0) {
        if (fsync(descriptor) != 0) return 4;
        syncs++;
    }
    uint64_t elapsed = monotonic_ns() - start;
    if (close(descriptor) != 0) return 4;
    emit("io", variant, writes + syncs, total, checksum, elapsed, "ok");
    free(buffer);
    return 0;
}

static pthread_mutex_t deadlock_a = PTHREAD_MUTEX_INITIALIZER;
static pthread_mutex_t deadlock_b = PTHREAD_MUTEX_INITIALIZER;

static void *deadlock_left(void *unused) {
    (void)unused;
    pthread_mutex_lock(&deadlock_a);
    struct timespec delay = {0, 100000000};
    nanosleep(&delay, NULL);
    pthread_mutex_lock(&deadlock_b);
    return NULL;
}

static void *deadlock_right(void *unused) {
    (void)unused;
    pthread_mutex_lock(&deadlock_b);
    struct timespec delay = {0, 100000000};
    nanosleep(&delay, NULL);
    pthread_mutex_lock(&deadlock_a);
    return NULL;
}

static int run_deadlock(void) {
    pthread_t left, right;
    if (pthread_create(&left, NULL, deadlock_left, NULL) != 0 ||
        pthread_create(&right, NULL, deadlock_right, NULL) != 0) return 3;
    pthread_join(left, NULL);
    pthread_join(right, NULL);
    return 5;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "probe required\n");
        return 2;
    }
    if (strcmp(argv[1], "locality") == 0) return run_locality(argc, argv);
    if (strcmp(argv[1], "allocation") == 0) return run_allocation(argc, argv);
    if (strcmp(argv[1], "contention") == 0) return run_contention(argc, argv);
    if (strcmp(argv[1], "io") == 0) return run_io(argc, argv);
    if (strcmp(argv[1], "deadlock") == 0) return run_deadlock();
    fprintf(stderr, "unknown probe: %s\n", argv[1]);
    return 2;
}
