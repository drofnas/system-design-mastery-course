from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from scripts import check_home_lab


def snapshot(platform_name="ubuntu", architecture="x86_64", **changes):
    value = {
        "platform": platform_name, "architecture": architecture, "ram_gib": 16.0,
        "logical_cpus": 4, "free_disk_gib": 40.0,
        "versions": {"python": "3.11.9", "git": "git version 2.45", "compiler": "cc 15.0",
                     "make": "GNU Make 4.4", "openssl": "OpenSSL 3.0", "docker": "Docker 28.0",
                     "node": "v24.19.0", "npm": "11.0"},
        "docker_daemon": True, "docker_memory_gib": 4.0, "openssl_addext": True,
        "loopback": True, "temporary_files": True, "repo_on_wsl_filesystem": True,
        "cgroup_controls": True, "chromium_available": True, "windows_browser_callback": True,
    }
    value.update(changes)
    return value


class PreflightTests(unittest.TestCase):
    def test_supported_platform_architecture_matrix(self):
        for platform_name, architecture in (("macos", "arm64"), ("macos", "x86_64"), ("ubuntu", "arm64"),
                                             ("ubuntu", "x86_64"), ("wsl2-ubuntu", "x86_64")):
            with self.subTest(platform=platform_name, architecture=architecture):
                self.assertEqual("pass", check_home_lab.evaluate(snapshot(platform_name, architecture), ["M03", "M15", "M16"])["summary"]["result"])

    def test_native_windows_is_blocked(self):
        report = check_home_lab.evaluate(snapshot("windows-native", "x86_64"), ["M02"])
        self.assertEqual("fail", report["summary"]["result"])
        self.assertIn("WSL2", " ".join(report["remediations"]))

    def test_windows_arm_wsl_is_out_of_scope(self):
        report = check_home_lab.evaluate(snapshot("wsl2-ubuntu", "arm64"), ["M02"])
        self.assertEqual("fail", report["summary"]["result"])

    def test_wsl1_is_not_mistaken_for_wsl2(self):
        report = check_home_lab.evaluate(snapshot("wsl1-unsupported", "x86_64"), ["M02"])
        self.assertEqual("fail", report["summary"]["result"])

    def test_unknown_resources_warn_but_do_not_block(self):
        report = check_home_lab.evaluate(snapshot(ram_gib=None, logical_cpus=None, free_disk_gib=None), ["M02"])
        self.assertEqual("warn", report["summary"]["result"])
        self.assertEqual(0, report["summary"]["fail"])

    def test_low_resources_and_missing_tools_block(self):
        values = snapshot(ram_gib=7.9, logical_cpus=1, free_disk_gib=19.9)
        values["versions"] = {key: None for key in values["versions"]}
        report = check_home_lab.evaluate(values, ["M03", "M05", "M16"])
        self.assertGreater(report["summary"]["fail"], 6)

    def test_incompatible_python_and_node_block(self):
        values = snapshot()
        values["versions"]["python"] = "3.10.14"
        values["versions"]["node"] = "v22.0.0"
        report = check_home_lab.evaluate(values, ["M16"])
        self.assertEqual("fail", report["summary"]["result"])

    def test_openssl_without_addext_is_incompatible(self):
        report = check_home_lab.evaluate(snapshot(openssl_addext=False), ["M05"])
        self.assertEqual("fail", report["summary"]["result"])

    def test_blocked_loopback_is_module_scoped(self):
        report = check_home_lab.evaluate(snapshot(loopback=False), ["M05"])
        self.assertEqual("fail", report["summary"]["result"])
        other = check_home_lab.evaluate(snapshot(loopback=False), ["M03"])
        self.assertEqual("skipped", next(item for item in other["checks"] if item["id"] == "loopback")["status"])

    def test_module_scope_skips_unneeded_toolchains(self):
        values = snapshot()
        values["versions"].update({"docker": None, "node": None, "npm": None, "openssl": None})
        report = check_home_lab.evaluate(values, ["M07"])
        self.assertEqual("pass", report["summary"]["result"])

    def test_json_contains_no_private_host_fields(self):
        report = check_home_lab.evaluate(snapshot(), ["M02"])
        rendered = json.dumps(report).lower()
        for forbidden in ("hostname", "username", "home_path", str(Path.home()).lower()):
            self.assertNotIn(forbidden, rendered)

    def test_cli_exit_codes_and_no_overwrite(self):
        with patch.object(check_home_lab, "collect_snapshot", return_value=snapshot()), redirect_stdout(StringIO()):
            self.assertEqual(0, check_home_lab.main(["--module", "M02", "--json"]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text("existing", encoding="utf-8")
            with patch.object(check_home_lab, "collect_snapshot", return_value=snapshot()):
                self.assertEqual(2, check_home_lab.main(["--module", "M02", "--json", "--output", str(path)]))
                self.assertEqual("existing", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
