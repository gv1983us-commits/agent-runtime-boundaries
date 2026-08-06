"""Structural canon checks for the Agent Runtime Boundaries artifact."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANON = ROOT / "CANON.md"
ARTIFACT = ROOT / "ARTIFACT.json"
RELATIONS = ROOT / "RELATIONS.md"
PROVENANCE = ROOT / "PROVENANCE.md"
README = ROOT / "README.md"
REFERENCES = ROOT / "references" / "RELATED_PUBLIC_SPECS.md"
PUBLICATION_MANIFEST = ROOT / "review" / "PUBLICATION_MANIFEST.md"
PROPOSAL = ROOT / "spec" / "03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md"

EXPECTED_ANALYTICAL = {
    "spec/00_SCOPE_AND_STATUS.md",
    "spec/01_FUNCTIONAL_BOUNDARIES.md",
    "spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md",
    "spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md",
}
EXPECTED_RELATIONS = {
    "claude.bec": (
        "gv1983us-commits/behavioral-execution-contract",
        "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261",
    ),
    "claude.mpaa": (
        "gv1983us-commits/mpaa",
        "0d1aaf35cc4826622f3312fdd2a1c2d40890b965",
    ),
    "claude.pca": (
        "gv1983us-commits/pca",
        "a669f023198615ad929f42df84f19380b57ca5ea",
    ),
    "claude.review_protocol": (
        "gv1983us-commits/repository-canon-review-protocol",
        "b4205ffd91a6316ab40243cbf8161a1c512cae1f",
    ),
    "claude.cdts": (
        "gv1983us-commits/cdts",
        "f91dbc003519efd5264655d905d0530dbfeac2fd",
    ),
}


class ArtifactCanonTests(unittest.TestCase):
    def test_required_canonical_surfaces_exist(self) -> None:
        for path in (
            CANON,
            ARTIFACT,
            RELATIONS,
            PROVENANCE,
            README,
            REFERENCES,
            PUBLICATION_MANIFEST,
            PROPOSAL,
        ):
            self.assertTrue(path.is_file(), f"missing {path.relative_to(ROOT)}")

    def test_machine_passport_declares_zero_normative_surfaces(self) -> None:
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(artifact["schema_version"], "1.0")
        self.assertEqual(artifact["artifact_id"], "claude.arb")
        self.assertEqual(artifact["repository"], "gv1983us-commits/agent-runtime-boundaries")
        self.assertEqual(artifact["artifact_version"], "0.3-draft")
        self.assertEqual(artifact["artifact_status"], "canonical_public_draft")
        self.assertEqual(artifact["specification_status"], "descriptive_analytical_companion")
        self.assertEqual(artifact["license"], "Apache-2.0")
        self.assertEqual(artifact["normative_surface_count"], 0)
        self.assertEqual(artifact["analytical_surface_count"], 4)
        self.assertEqual(artifact["proposal_surface_count"], 1)
        self.assertIn("zero_normative_surfaces", artifact["normative_authority_model"])
        self.assertEqual(
            {item["path"] for item in artifact["analytical_surfaces"]},
            EXPECTED_ANALYTICAL,
        )
        self.assertFalse(artifact["reference_implementation"]["normative"])

    def test_proposal_is_explicitly_unadopted(self) -> None:
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(len(artifact["proposal_surfaces"]), 1)
        proposal = artifact["proposal_surfaces"][0]
        self.assertEqual(proposal["path"], "spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md")
        self.assertEqual(proposal["proposal_id"], "ARB-03")
        self.assertFalse(proposal["adopted"])
        self.assertFalse(proposal["normative_owner_selected"])
        self.assertFalse(proposal["multi_implementation_conformance_claimed"])

        text = PROPOSAL.read_text(encoding="utf-8")
        self.assertIn("PUBLIC DRAFT — PROPOSAL", text)
        self.assertIn("illustrative proposal", text)
        self.assertIn("does not select a normative owner", text)
        self.assertIn("remains a proposal", text)

    def test_all_five_neighbor_relations_are_fixed_and_non_importing(self) -> None:
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        relations = {item["artifact_id"]: item for item in artifact["relations"]}
        self.assertEqual(set(relations), set(EXPECTED_RELATIONS))
        for artifact_id, (repository, revision) in EXPECTED_RELATIONS.items():
            with self.subTest(artifact_id=artifact_id):
                relation = relations[artifact_id]
                self.assertEqual(relation["repository"], repository)
                self.assertEqual(relation["reviewed_revision"], revision)
                self.assertRegex(revision, r"^[0-9a-f]{40}$")
                self.assertFalse(relation["conclusion_imported"])

    def test_source_receipt_and_relation_surface_use_current_revisions(self) -> None:
        reference_text = REFERENCES.read_text(encoding="utf-8")
        relation_text = RELATIONS.read_text(encoding="utf-8")
        for artifact_id, (repository, revision) in EXPECTED_RELATIONS.items():
            with self.subTest(artifact_id=artifact_id):
                self.assertIn(repository, reference_text)
                self.assertIn(revision, reference_text)
                self.assertIn(repository, relation_text)
                self.assertIn(revision, relation_text)
        self.assertIn("2026-08-06", reference_text)
        self.assertIn("CDTS", reference_text)

    def test_assertion_boundaries_all_remain_false(self) -> None:
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertTrue(artifact["assertion_boundaries"])
        self.assertTrue(all(value is False for value in artifact["assertion_boundaries"].values()))

    def test_human_surfaces_publish_analytical_authority_and_limits(self) -> None:
        canon = CANON.read_text(encoding="utf-8")
        readme = README.read_text(encoding="utf-8")
        relations = RELATIONS.read_text(encoding="utf-8")
        provenance = PROVENANCE.read_text(encoding="utf-8")
        manifest = PUBLICATION_MANIFEST.read_text(encoding="utf-8")

        for text in (canon, readme):
            self.assertIn("0.3-draft", text)
            self.assertIn("canonical_public_draft", text)
            self.assertIn("zero", text.lower())
            self.assertIn("normative", text.lower())
            self.assertIn("ARB-03", text)

        self.assertIn("normative_surface_count = 0", canon)
        self.assertIn("CDTS", relations)
        self.assertIn("Apache-2.0", provenance)
        self.assertIn("0 normative surfaces", manifest)
        self.assertIn("No independent analytical-truth claim", manifest)

    def test_claim_classes_remain_complete_and_distinct(self) -> None:
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(
            artifact["claim_classes"],
            [
                "OBSERVATION",
                "FUNCTIONAL_RECONSTRUCTION",
                "ANALYTICAL_INTERPRETATION",
                "PROPOSAL",
                "UNKNOWN",
            ],
        )
        scope = (ROOT / "spec" / "00_SCOPE_AND_STATUS.md").read_text(encoding="utf-8")
        for claim_class in artifact["claim_classes"]:
            self.assertIn(claim_class, scope)

    def test_rejected_inference_chain_is_published(self) -> None:
        mapping = (ROOT / "spec" / "04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md").read_text(
            encoding="utf-8"
        )
        for marker in (
            "reasoning about an action != execution",
            "visible status != execution evidence",
            "delivered != persisted",
            "persisted != retrievable",
            "retrievable != admitted into working state",
            "working state present != committed",
            "committed != PCA process continuation",
            "ARB is not a normative owner",
        ):
            self.assertIn(marker, mapping)


if __name__ == "__main__":
    unittest.main()
