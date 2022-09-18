from app.database import get_session
from app.models.human import HumanModel
from app.tests.utils import BaseTestCase
from app.services.stat import StatService


class TestStatService(BaseTestCase):
    """Class to manage Stat Service tests."""

    def test_get_stats_two_humans_one_mutant(self):
        """Tests get Stats with two humans and one mutant."""

        dna = ["GGGGCC", "AAATAT", "GCGCGC", "ATATAT", "GCGCGC", "ATATAT"]
        with get_session() as session:
            human = HumanModel(dna=dna, is_mutant=False)
            mutant = HumanModel(dna=dna, is_mutant=True)
            session.add(human)
            session.add(mutant)
            session.commit()

        stats = StatService.get_stats()
        assert stats['count_mutant_dna'] == 1
        assert stats['count_human_dna'] == 2
        assert stats['ratio'] == 0.5

    def test_get_stats_two_humans_two_mutants(self):
        """Tests get Stats with two humans and two mutants."""

        dna = ["GGGGCC", "AAATAT", "GCGCGC", "ATATAT", "GCGCGC", "ATATAT"]
        with get_session() as session:
            human = HumanModel(dna=dna, is_mutant=True)
            mutant = HumanModel(dna=dna, is_mutant=True)
            session.add(human)
            session.add(mutant)
            session.commit()

        stats = StatService.get_stats()
        assert stats['count_mutant_dna'] == 2
        assert stats['count_human_dna'] == 2
        assert stats['ratio'] == 1

    def test_get_stats_without_humans(self):
        """Tests get Stats without humans."""

        stats = StatService.get_stats()
        assert stats['count_mutant_dna'] == 0
        assert stats['count_human_dna'] == 0
        assert stats['ratio'] == 0
