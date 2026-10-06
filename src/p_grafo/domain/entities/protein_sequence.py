"""Protein sequence entity."""

from dataclasses import dataclass

from p_grafo.domain.exceptions.invalid_protein_sequence import InvalidProteinSequenceError

# Twenty canonical residues. Ambiguous and non-standard codes are rejected.
CANONICAL_RESIDUES = frozenset("ACDEFGHIKLMNPQRSTVWY")


@dataclass(frozen=True, slots=True)
class ProteinSequence:
    """Validated amino-acid sequence, independent of file formats."""

    identifier: str
    sequence: str

    def __post_init__(self) -> None:
        normalised = "".join(self.sequence.split()).upper()
        if not normalised:
            raise InvalidProteinSequenceError("Protein sequence must not be empty.")
        invalid = tuple(
            residue for residue in sorted(set(normalised)) if residue not in CANONICAL_RESIDUES
        )
        if invalid:
            residues = ", ".join(invalid)
            raise InvalidProteinSequenceError(
                f"Protein sequence contains invalid residues: {residues}."
            )
        object.__setattr__(self, "sequence", normalised)

    @property
    def length(self) -> int:
        """Return the number of residues in the normalised sequence."""
        return len(self.sequence)
