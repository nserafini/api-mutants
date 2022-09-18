import pytest
from app.tests.utils import BaseTestCase
from app.services.human import HumanService


class TestHumanService(BaseTestCase):
    """Class to manage Human Service tests."""

    def test_is_mutant(self):
        """Tests is Mutant."""

        dna = ["TAAAAT", "GGCCCC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        assert HumanService(dna).is_mutant() is True

    def test_is_not_mutant(self):
        """Tests is not Mutant."""

        dna = ["GGGGCC", "AAATAT", "GCGCGC", "ATATAT", "GCGCGC", "ATATAT"]
        assert HumanService(dna).is_mutant() is False

    def test_invalid_table_size(self):
        """Tests invalid table size."""

        dna = ["AAA", "GCG", "GTA"]
        with pytest.raises(ValueError):
            HumanService(dna).is_mutant()

    def test_invalid_row_length(self):
        """Tests invalid row length."""

        row_of_four = "AAAA"
        dna = ["AAAAAT", row_of_four, "GTATAT", "GCGCGC", "GTATAT", "CCGCGC"]
        with pytest.raises(ValueError):
            HumanService(dna).is_mutant()

    def test_invalid_character(self):
        """Tests invalid character."""

        x = 'X'
        dna = ["AAAAAT", "GCGCGG", "GTATAT", "GCGCGC", "GTATAT", ("CCGCG" + x)]
        with pytest.raises(ValueError):
            HumanService(dna).is_mutant()

    def test_is_not_mutant_with_two_sequences_of_three(self):
        """Tests is not Mutant with Two Sequences of Three."""

        dna = ["TAAATT", "GAGCCC", "TTATGT", "AGAAGG", "TCACTG", "TCACTG"]
        assert HumanService(dna).is_mutant() is False

    def test_is_mutant_with_one_horizontal_and_one_vertical_sequence(self):
        """Tests is Mutant with one Horizontal and one Vertical Sequences."""

        dna = ["ATATAT", "GCGCGT", "ATATAT", "ACGCGT", "ATATAT", "ACGCGC"]
        assert HumanService(dna).is_mutant() is True

    def test_is_not_mutant_with_only_one_horizontal_five_letters_sequence(self):
        """Tests is not Mutant with only one Horizontal of Five letters Sequence."""

        dna = ["ATATAT", "GGGGGC", "ATATAT", "GCGCGC", "ATATAT", "GCGCGC"]
        assert HumanService(dna).is_mutant() is False

    def test_is_not_mutant_with_only_one_vertical_five_letters_sequence(self):
        """Tests is not Mutant with only one Vertical of Five letters Sequence."""

        dna = ["ATATAT", "ACGCGC", "ATATAT", "ACGCGC", "ATATAT", "GCGCGC"]
        assert HumanService(dna).is_mutant() is False

    def test_is_mutant_with_one_sequence_of_five_and_one_sequence_of_four(self):
        """Tests is Mutant with one of Five letters and one of four letters Sequence."""

        dna = ["AAAAAT", "GCGCGC", "GTATAT", "GCGCGC", "GTATAT", "CCGCGC"]
        assert HumanService(dna).is_mutant() is True

    def test_is_not_mutant_with_no_sequences_in_nine_row_table(self):
        """Tests is not Mutant with table of nine rows."""

        dna = ["ATATATATA", "CGCGCGCGC", "ATATATATA", "CGCGCGCGC", "ATATATATA", "CGCGCGCGC", "ATATATATA", "CGCGCGCGC", "ATATATATA"]
        assert HumanService(dna).is_mutant() is False

    def test_is_mutant_with_two_consecutive_horizontal_sequences(self):
        """Tests is Mutant with two consecutives horizontal Sequences."""

        dna = ["ATATATATA", "CGGGGGGGG", "ATATATATA", "CGCGCGCGC", "ATATATATA", "CGCGCGCGC", "ATATATATA", "CGCGCGCGC", "ATATATATA"]
        assert HumanService(dna).is_mutant() is True

    def test_is_mutant_with_two_consecutive_vertical_sequences(self):
        """Tests is Mutant with two consecutives vertical Sequences."""

        dna = ["ATATATATA", "CGCGCGCGC", "ATATATAGA", "CGCGCGCGC", "ATATATAGA", "CGCGCGCGC", "ATATATAGA", "CGCGCGCGC", "ATATATAGA"]
        assert HumanService(dna).is_mutant() is True
