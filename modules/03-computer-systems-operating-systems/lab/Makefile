PYTHON ?= python3
CC ?= cc
CFLAGS ?= -std=c11 -O2 -Wall -Wextra -Werror -pthread

.PHONY: build test sanitize matrix clean

build:
	mkdir -p build
	$(CC) $(CFLAGS) src/systems_probe.c -o build/systems_probe

test: build
	PYTHONPATH=. $(PYTHON) -m unittest discover -s tests -v

sanitize:
	mkdir -p build
	$(CC) $(CFLAGS) -fsanitize=address,undefined -fno-omit-frame-pointer src/systems_probe.c -o build/systems_probe-sanitize
	./build/systems_probe-sanitize locality contiguous 10000 1
	./build/systems_probe-sanitize allocation reuse 1000 4096
	./build/systems_probe-sanitize contention sharded 4 10000

matrix: build
	PYTHONPATH=. $(PYTHON) -m systems_lab matrix --manifest scenarios/required-matrix.json --output-dir build/matrix

clean:
	rm -rf build
