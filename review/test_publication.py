#!/usr/bin/env python3
"""Publication-discipline checks for the analytical ARB companion."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "spec" / "04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md"
REFERENCES = ROOT / "references" / "RELATED_PUBLIC_SPECS.md"

STALE_PCA_NAME = "Persistent" + " Continuity Architecture"

PINNED = {
    "MPAA": "1d369f6cd091b99f9492cfaf730f0a170b55106e",
    "PCA": "6ad1a86d7c09b36839d162c580f84f05cfe4a598",
    "BEC": "bb46f5f8aac96d1cffba7a334c5d17fb331ef3af",
    "Review Protocol": "595c08b877e4dfb14593454c2eec7c8f5df46c28",
}
REQUIRED_MAPPING_HEADINGS = (
    "## 1. MPAA ↔ BEC",
    "## 2. MPAA ↔ PCA",
    "## 3. BEC ↔ PCA",
    "## 4. ARB-03 closure proposal ↔ normative domains",
)
REQUIRED_TERMS = (
    "capability",
    "authorization",
    "invocation",
    "evidence",
    "verification",
    "result",
    "identity-profile continuity",
    "process continuation",
    "`closed`",
    "`committed`",
    "`delivered`",
    "`persisted`",
    "`retrievable`",
    "working state",
    "PCA `CORPUS`",
    "ARB `PERSISTENT CORPUS`",
)


def public_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts:
            yield path


class PublicationChecks(unittest.TestCase):
    def test_mapping_surface_exists(self):
        self.assertTrue(MAPPING.is_file(), "cross-specification mapping is missing")

    def test_references_pin_current_accepted_commits(self):
        text = REFERENCES.read_text(encoding="utf-8")
        for owner, sha in PINNED.items():
            self.assertIn(sha, text, f"{owner} is not pinned to accepted commit {sha}")

    def test_mapping_has_four_required_tables_and_terms(self):
        text = MAPPING.read_text(encoding="utf-8")
        for heading in REQUIRED_MAPPING_HEADINGS:
            self.assertIn(heading, text)
        for term in REQUIRED_TERMS:
            self.assertIn(term, text)
        for sha in PINNED.values():
            self.assertIn(sha, text)
        for source_path in (
            "spec/00_SESSION_BOOTSTRAP.md",
            "spec/02_IDENTITY_PROFILE_SPEC.md",
            "spec/03_RUNTIME_CONTRACT.md",
            "spec/05_RUNTIME_REPORT_SCHEMA.md",
            "spec/01_BEC_COMPACT_CORE.md",
            "conformance/README.md",
            "spec/01_PCA_CORE.md",
            "repository-canon-and-review-protocol-v0.1.md",
        ):
            self.assertIn(source_path, text)
        pinned_roots = (
            f"https://github.com/gv1983us-commits/mpaa/tree/{PINNED['MPAA']}",
            f"https://github.com/gv1983us-commits/pca/tree/{PINNED['PCA']}",
            f"https://github.com/gv1983us-commits/behavioral-execution-contract/tree/{PINNED['BEC']}",
            f"https://github.com/gv1983us-commits/repository-canon-review-protocol/tree/{PINNED['Review Protocol']}",
        )
        reference_text = REFERENCES.read_text(encoding="utf-8")
        for url in pinned_roots:
            self.assertIn(url, text)
            self.assertIn(url, reference_text)

    def test_arb_does_not_claim_normative_ownership(self):
        text = MAPPING.read_text(encoding="utf-8").lower()
        required_boundaries = (
            "analytical companion",
            "does not transfer normative ownership",
            "does not select a normative home",
            "no equivalence",
        )
        for boundary in required_boundaries:
            self.assertIn(boundary, text)

    def test_no_stale_pca_nomenclature(self):
        for path in public_files():
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(STALE_PCA_NAME, text, str(path.relative_to(ROOT)))

    def test_no_local_path_or_credential_markers(self):
        forbidden = re.compile(
            r"(C:\\Users\\|/c/Users/|/Users/|/home/|AppData|credentials\.json|"
            r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY|ghp_[A-Za-z0-9]+|"
            r"api[_-]?key\s*[:=]|access[_-]?token\s*[:=])",
            re.IGNORECASE,
        )
        for path in public_files():
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(forbidden.search(text), str(path.relative_to(ROOT)))

    def test_markdown_integrity_and_relative_links(self):
        link_re = re.compile(r"\[[^\]]*\]\((?!https?://|mailto:|#)([^)]+)\)")
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.endswith("\n"), f"no final newline: {path.relative_to(ROOT)}")
            self.assertEqual(0, text.count("```") % 2, f"unbalanced fences: {path.relative_to(ROOT)}")
            table = []
            for number, line in enumerate(text.splitlines() + [""], 1):
                self.assertEqual(line.rstrip(), line, f"trailing whitespace: {path.relative_to(ROOT)}:{number}")
                if line.startswith("|") and line.endswith("|"):
                    table.append((number, line.count("|")))
                elif table:
                    self.assertEqual(1, len({count for _, count in table}), f"malformed table: {path.relative_to(ROOT)}:{table[0][0]}")
                    table = []
            for target in link_re.findall(text):
                relative = target.split("#", 1)[0]
                if relative:
                    self.assertTrue((path.parent / relative).resolve().exists(), f"broken link: {path.relative_to(ROOT)} -> {target}")

    def test_spec_documents_declare_status_and_mode(self):
        for path in (ROOT / "spec").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn("**Status:**", text, str(path.relative_to(ROOT)))
            self.assertIn("**Mode:**", text, str(path.relative_to(ROOT)))

    def test_entry_points_expose_mapping_and_proposal_boundary(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        closure = (ROOT / "spec" / "03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md").read_text(encoding="utf-8")
        self.assertIn("04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md", readme)
        self.assertIn("04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md", closure)
        for term in ("`closed`", "`committed`", "`delivered`", "`persisted`", "`retrievable`"):
            self.assertIn(term, closure)
        self.assertIn("does not select a normative owner", closure)

    def test_ci_and_manifest_cover_publication_checker(self):
        workflow = ROOT / ".github" / "workflows" / "docs.yml"
        self.assertTrue(workflow.is_file(), "docs CI workflow is missing")
        manifest = (ROOT / "review" / "PUBLICATION_MANIFEST.md").read_text(encoding="utf-8")
        for path in (
            "spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md",
            "review/2026-07-26_MAPPING_UPDATE_REVIEW.md",
            "review/test_publication.py",
            ".github/workflows/docs.yml",
        ):
            self.assertIn(path, manifest)
        self.assertIn("No independent content-review claim", manifest)


if __name__ == "__main__":
    unittest.main()
