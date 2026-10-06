"""Domain exception for an invalid protein sequence."""


class InvalidProteinSequenceError(ValueError):
    """Raised when a protein sequence is empty or contains a non-canonical residue."""
