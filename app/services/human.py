from app.database import get_session
from app.models.human import HumanModel


class HumanService:
    """Class to manage Human Service."""

    dna = []

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
        """Check if DNA is Mutant."""

        return True