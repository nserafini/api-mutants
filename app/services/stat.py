from app.logger import Logger


class StatService:
    """Class to manage Human Service."""

    logger = Logger.get_logger()

    @classmethod
    def get_stats(cls):
        """Retrieves Stats."""

        return {
            "count_mutant_dna": 0,
            "count_human_dna": 0,
            "ratio": 0
        }