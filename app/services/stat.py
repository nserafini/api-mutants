from app.database import get_session
from app.logger import Logger
from app.models.human import HumanModel


class StatService:
    """Class to manage Human Service."""

    logger = Logger.get_logger()

    @classmethod
    def get_stats(cls):
        """Retrieves Stats."""

        with get_session() as session:
            mutant_dnas = session.query(HumanModel).filter_by(
                **{'is_mutant': True}).count()
            human_dnas = session.query(HumanModel).count()

        ratio = 0
        if human_dnas > 0:
            ratio = round(mutant_dnas / human_dnas, 2)

        return {
            "count_mutant_dna": mutant_dnas,
            "count_human_dna": human_dnas,
            "ratio": ratio
        }
