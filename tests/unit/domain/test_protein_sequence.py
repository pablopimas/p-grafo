"""Unit tests for ProteinSequence."""

import pytest

from p_grafo.domain.entities.protein_sequence import ProteinSequence
from p_grafo.domain.exceptions.invalid_protein_sequence import InvalidProteinSequenceError


def test_accepts_a_valid_sequence() -> None:
    protein = ProteinSequence(identifier="seq-1", sequence="ACDEFGHIK")

    assert protein.identifier == "seq-1"
    assert protein.sequence == "ACDEFGHIK"


def test_normalises_lowercase_input() -> None:
    protein = ProteinSequence(identifier="seq-1", sequence="acdefghik")

    assert protein.sequence == "ACDEFGHIK"


def test_removes_whitespace() -> None:
    protein = ProteinSequence(identifier="seq-1", sequence="ACD EFG\nHIK\t")

    assert protein.sequence == "ACDEFGHIK"


def test_rejects_an_empty_sequence() -> None:
    with pytest.raises(InvalidProteinSequenceError, match="must not be empty"):
        ProteinSequence(identifier="seq-1", sequence="   \n\t")


def test_rejects_invalid_residues() -> None:
    with pytest.raises(InvalidProteinSequenceError, match="invalid residues: B, X"):
        ProteinSequence(identifier="seq-1", sequence="ACX B")


def test_exposes_correct_sequence_length() -> None:
    protein = ProteinSequence(identifier="seq-1", sequence="ac de")

    assert protein.length == 4
