import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_resources as verifier


class ResourceVerificationTests(unittest.TestCase):
    def resource(self, *, title="Expected Title", publisher="Expected Publisher"):
        return {
            "id": "RES-01",
            "title": title,
            "author_or_publisher": publisher,
            "url": "https://official.example/source",
            "final_url": "https://official.example/source",
            "required": True,
            "assignment": "Read the bounded primary-source section.",
            "text_alternative": "fallback.md",
        }

    def record(self, resource):
        return {
            "module": "M01",
            "resource_id": "RES-01",
            "resource_key": "M01/RES-01",
            "kind": "assigned_resource",
            "required": True,
            "blocking": True,
            "declared_title": resource["title"],
            "declared_publisher": resource["author_or_publisher"],
            "requested_url": resource["url"],
            "declared_final_url": resource["final_url"],
            "local_fallback": "fallback.md",
        }

    def test_body_wide_title_and_publisher_text_is_not_accepted(self):
        resource = self.resource()
        body = b"<html><head><title>Different Work</title></head><body>Expected Title Expected Publisher</body></html>"
        inspected = verifier.inspect_body(
            self.record(resource), resource, status=200,
            final_url=resource["url"], content_type="text/html", body=body,
        )
        self.assertFalse(inspected["title_match"])
        self.assertFalse(inspected["publisher_match"])

    def test_explicit_compound_host_authority_can_supply_missing_publisher_metadata(self):
        resource = self.resource(
            title="The tokenization pipeline",
            publisher="Hugging Face",
        )
        resource["url"] = "https://huggingface.co/learn/llm-course/chapter2/4"
        resource["final_url"] = resource["url"]
        body = b"<html><head><title>The tokenization pipeline</title></head><body></body></html>"
        inspected = verifier.inspect_body(
            self.record(resource), resource, status=200,
            final_url=resource["url"], content_type="text/html", body=body,
        )
        self.assertTrue(inspected["title_match"])
        self.assertTrue(inspected["publisher_match"])

    def test_explicit_host_authority_does_not_accept_a_different_publisher(self):
        resource = self.resource(
            title="The tokenization pipeline",
            publisher="Unrelated Publisher",
        )
        resource["url"] = "https://huggingface.co/learn/llm-course/chapter2/4"
        resource["final_url"] = resource["url"]
        body = b"<html><head><title>The tokenization pipeline</title></head><body></body></html>"
        inspected = verifier.inspect_body(
            self.record(resource), resource, status=200,
            final_url=resource["url"], content_type="text/html", body=body,
        )
        self.assertTrue(inspected["title_match"])
        self.assertFalse(inspected["publisher_match"])

    def test_authority_alias_rejects_a_lookalike_host(self):
        resource = self.resource(
            title="The tokenization pipeline",
            publisher="Hugging Face",
        )
        resource["url"] = "https://huggingface.co.evil.example/learn/llm-course/chapter2/4"
        resource["final_url"] = resource["url"]
        body = b"<html><head><title>The tokenization pipeline</title></head><body></body></html>"
        inspected = verifier.inspect_body(
            self.record(resource), resource, status=200,
            final_url=resource["url"], content_type="text/html", body=body,
        )
        self.assertTrue(inspected["title_match"])
        self.assertFalse(inspected["publisher_match"])

    def test_changed_binary_hash_rejects_manual_attestation(self):
        resource = self.resource()
        payload = b"current binary bytes"
        record = verifier.inspect_body(
            self.record(resource), resource, status=200,
            final_url=resource["url"], content_type="application/pdf", body=payload,
        )
        attestation = {
            "resource_key": "M01/RES-01",
            "requested_url": resource["url"],
            "content_sha256": hashlib.sha256(b"old binary bytes").hexdigest(),
            "verified_title": resource["title"],
            "verified_publisher": resource["author_or_publisher"],
        }
        with tempfile.TemporaryDirectory() as directory, patch.object(verifier, "ROOT", Path(directory)):
            (Path(directory) / "fallback.md").write_text("fallback", encoding="utf-8")
            failures, _ = verifier.evaluate_records([record], {"M01/RES-01": attestation})
        self.assertTrue(any("content-hash attestation" in failure for failure in failures))

    def test_inaccessible_blocking_source_without_fallback_fails(self):
        resource = self.resource()
        record = self.record(resource)
        record.update({"access": "failed", "status": 503})
        with tempfile.TemporaryDirectory() as directory, patch.object(verifier, "ROOT", Path(directory)):
            failures, _ = verifier.evaluate_records([record], {})
        self.assertTrue(any("could not be retrieved" in failure for failure in failures))

    def test_unregistered_authored_url_is_discovered(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet"], cwd=root, check=True)
            (root / "lesson.md").write_text(
                "Use [an unmapped source](https://facts.example/claim#section).\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "add", "lesson.md"], cwd=root, check=True)
            observed = verifier.scan_markdown_urls(root)
        self.assertEqual(observed, {"https://facts.example/claim": ["lesson.md"]})


if __name__ == "__main__":
    unittest.main()
