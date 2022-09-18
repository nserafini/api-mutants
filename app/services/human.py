from app.database import get_session
from app.models.human import HumanModel


class HumanService:
    """Class to manage Human Service."""

    dna = []
    sequence_length = 4

    def __init__(self, dna):
        """Init Human."""

        self.dna = dna

    def save(self):
        """Creates a Human."""

        with get_session() as session:
            human = HumanModel(
                dna=','.join(self.dna), 
                is_mutant=self.is_mutant()
            )
            session.add(human)
            session.commit()
        return human

    def is_mutant(self):
        """Checks if DNA is Mutant."""

        self.check_table_size()
        return True

    def check_table_size(self):
        """Checks DNA table size."""

        if len(self.dna) < self.sequence_length:
            raise ValueError(f"Table min length must be {self.sequence_length}x{self.sequence_length}")
