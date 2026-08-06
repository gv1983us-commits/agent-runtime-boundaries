#!/usr/bin/env python3
"""Publication-discipline checks for the analytical ARB companion."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "spec" / "04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md"
REFERENCES = ROOT / "references" / "RELATED_PUBLIC_SPECS.md"
CANON = ROOT / "CANON.md"
ARTIFACT = ROOT / "ARTIFACT.json"
RELATIONS = ROOT / "RELATIONS.md"
PROPOSAL = ROOT / "spec" / "03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md"
MANIFEST = ROOT / "review" / "PUBLICATION_MANIFEST.md"

STALE_PCA_NAME = "Persistent" + " Continuity Architecture"

PINNED = {
    "BEC": "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261",
    "MPAA": "0d1aaf35cc4826622f3312fdd2a1c2d40890b965",
    "PCA": "a669f023198615ad929f42df84f19380b57ca5ea",
    "Review Protocol": "b4205ffd91a6316ab40243cbf8161a1c512cae1f",
    "CDTS": "f91dbc003519efd5264655d905d0530dbfeac2fd",
}
REPOSITORIES = {
    "BEC": "gv1983us-commits/behavioral-execution-contract",
    "MPAA": "gv1983us-commits/mpaa",
    "PCA": "gv1983us-commits/pca",
    "Review Protocol": "gv1983us-commits/repository-canon-review-protocol",
    "CDTS": "gv1983us-commits/cdts",
}
REQUIRED_MAPPING_HEADINGS = (
    "## 4. ARB ↔ BEC",
    "## 5. ARB ↔ MPAA",
    "## 6. ARB ↔ PCA",
    "## 7. ARB ↔ Review Protocol",
    "## 8. ARB ↔ CDTS",
    "## 9. ARB-03 closure proposal",
    "## 10. Rejected composite inferences",
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
    "ARB is not a normative owner",
)


def public_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts:
            yield path


class PublicationChecks(unittest.TestCase):
    def test_canonical_surfaces_exist(self):
        for path in (CANON, ARTIFACT, RELATIONS, MAPPING, REFERENCES, PROPOSAL, MANIFEST):
            self.assertTrue(path.is_file(), f"missing {path.relative_to(ROOT)}")

    def test_references_pin_current_five_source_set(self):
        text = REFERENCES.read_text(encoding="utf-8")
        self.assertIn("2026-08-06", text)
        for owner, sha in PINNED.items():
            with self.subTest(owner=owner):
                self.assertIn(sha, text, f"{owner} is not pinned to {sha}")
                self.assertIn(REPOSITORIES[owner], text)
                root = f"https://github.com/{REPOSITORIES[owner]}/tree/{sha}"
                self.assertIn(root, text)

    def test_mapping_has_five_neighbor_sections_and_required_terms(self):
        text = MAPPING.read_text(encoding="utf-8")
        for heading in REQUIRED_MAPPING_HEADINGS:
            self.assertIn(heading, text)
        for term in REQUIRED_TERMS:
            self.assertIn(term, text)
        for owner, sha in PINNED.items():
            with self.subTest(owner=owner):
                self.assertIn(sha, text)
                self.assertIn(REPOSITORIES[owner], REFERENCES.read_text(encoding="utf-8"))

    def test_mapping_publishes_rejected_inference_chain(self):
        text = MAPPING.read_text(encoding="utf-8")
        for marker in (
            "reasoning about an action != execution",
            "visible status != execution evidence",
            "delivered != persisted",
            "persisted != retrievable",
            "retrievable != admitted into working state",
            "working state present != committed",
            "committed != PCA process continuation",
            "process continuation != identity-profile continuity",
        ):
            self.assertIn(marker, text)

    def test_arb_does_not_claim_normative_ownership(self):
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(artifact["normative_surface_count"], 0)
        self.assertFalse(artifact["reference_implementation"]["normative"])
        self.assertTrue(all(value is False for value in artifact["assertion_boundaries"].values()))

        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (CANON, RELATIONS, MAPPING, PROPOSAL)
        ).lower()
        for boundary in (
            "zero normative",
            "does not transfer normative ownership",
            "arb is not a normative owner",
            "does not select a normative owner",
            "no equivalence",
        ):
            self.assertIn(boundary, combined)

    def test_proposal_remains_explicitly_unadopted(self):
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(len(artifact["proposal_surfaces"]), 1)
        proposal_record = artifact["proposal_surfaces"][0]
        self.assertFalse(proposal_record["adopted"])
        self.assertFalse(proposal_record["normative_owner_selected"])
        self.assertFalse(proposal_record["multi_implementation_conformance_claimed"])

        text = PROPOSAL.read_text(encoding="utf-8")
        for marker in (
            "PUBLIC DRAFT — PROPOSAL",
            "**Adopted:** No",
            "**Normative owner selected:** No",
            "illustrative proposal",
            "remains a proposal",
        ):
            self.assertIn(marker, text)

    def test_all_relations_are_fixed_and_non_importing(self):
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        relations = {item["artifact_id"]: item for item in artifact["relations"]}
        self.assertEqual(
            set(relations),
            {
                "claude.bec",
                "claude.mpaa",
                "claude.pca",
                "claude.review_protocol",
                "claude.cdts",
            },
        )
        for item in relations.values():
            self.assertRegex(item["reviewed_revision"], r"^[0-9a-f]{40}$")
            self.assertFalse(item["conclusion_imported"])

    def test_no_stale_pca_nomenclature(self):
        for path in public_files():
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(STALE_PCA_NAME, text, str(path.relative_to(ROOT)))

    def test_no_local_path_or_credential_markers(self):
        forbidden = re.compile(
            r"(C:\\Users\\|/c/Users/|/Users/|/home/|AppData|credentials\.json|"
            r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY|ghp_[A-Za-z0-9]{10,}|"
            r"github_pat_[A-Za-z0-9_]{10,}|(?<![A-Za-z0-9])sk-[A-Za-z0-9]{10,}|"
            r"AKIA[0-9A-Z]{16}|api[_-]?key\s*[:=]|access[_-]?token\s*[:=])",
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
                stripped = line.rstrip(" \t")
                trailing = line[len(stripped):]
                self.assertIn(
                    trailing,
                    ("", "  "),
                    f"unsupported trailing whitespace: {path.relative_to(ROOT)}:{number}",
                )
                if line.startswith("|") and line.endswith("|"):
                    table.append((number, line.count("|")))
                elif table:
                    self.assertEqual(
                        1,
                        len({count for _, count in table}),
                        f"malformed table: {path.relative_to(ROOT)}:{table[0][0]}",
                    )
                    table = []
            for target in link_re.findall(text):
                relative = target.split("#", 1)[0]
                if relative:
                    self.assertTrue(
                        (path.parent / relative).resolve().exists(),
                        f"broken link: {path.relative_to(ROOT)} -> {target}",
                    )

    def test_spec_documents_declare_status_mode_and_version(self):
        for path in (ROOT / "spec").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn("**Status:**", text, str(path.relative_to(ROOT)))
            self.assertIn("**Mode:**", text, str(path.relative_to(ROOT)))
            self.assertIn("**Version:** 0.3", text, str(path.relative_to(ROOT)))

    def test_entry_points_expose_canon_mapping_and_proposal_boundary(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for text in (readme, agents):
            self.assertIn("CANON.md", text)
            self.assertIn("ARTIFACT.json", text)
            self.assertIn("04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md", text)
            self.assertIn("normative_surface_count", text)
            self.assertIn("ARB-03", text)
            self.assertIn("CDTS", text)

    def test_ci_and_manifest_cover_complete_checker(self):
        workflow = ROOT / ".github" / "workflows" / "docs.yml"
        self.assertTrue(workflow.is_file(), "docs CI workflow is missing")
        manifest = MANIFEST.read_text(encoding="utf-8")
        for path in (
            "CANON.md",
            "ARTIFACT.json",
            "RELATIONS.md",
            "PROVENANCE.md",
            "spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md",
            "review/2026-08-06_CANONIZATION_REVIEW.md",
            "review/test_publication.py",
            "review/test_artifact_canon.py",
            ".github/workflows/docs.yml",
        ):
            self.assertIn(path, manifest)
        self.assertIn("No independent analytical-truth claim", manifest)
        self.assertIn("0 normative surfaces", manifest)

    def test_license_is_declared_and_present(self):
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(artifact["license"], "Apache-2.0")
        self.assertTrue((ROOT / "LICENSE").is_file())
        self.assertIn("Apache License", (ROOT / "LICENSE").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
