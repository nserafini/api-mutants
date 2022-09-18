from app.database import get_session
from app.models.human import HumanModel


class HumanService:
    """Class to manage Human Service."""

    dna = []
    valid_letters = ['A', 'T', 'C', 'G']
    sequence_length = 4
    min_sequence_match = 2
    founded_sequences = 0
    consecutive_letters = 0

    def __init__(self, dna):
        """Init Human."""

        self.dna = dna

    def save(self):
        """Creates a Human."""

        with get_session() as session:
            human = session.query(HumanModel).filter_by(
                **{'dna': self.dna}).first()
            if not human:
                human = HumanModel(
                    dna=self.dna, 
                    is_mutant=self.is_mutant()
                )
                session.add(human)
                session.commit()
        return human

    def is_mutant(self):
        """Checks if DNA is Mutant."""

        is_mutant = False
        self.founded_sequences = 0

        self.check_table_size()
        self.scan_rows()
        self.scan_columns()
        self.scan_up_foward_diagonals()
        self.scan_down_foward_diagonals()

        if self.founded_sequences >= self.min_sequence_match:
            is_mutant = True
        return is_mutant

    def check_table_size(self):
        """Checks DNA table size."""

        if len(self.dna) < self.sequence_length:
            raise ValueError(f"Table min length must be {self.sequence_length}x{self.sequence_length}")

    def scan_rows(self):
        """Scans rows."""

        for i in range(0, len(self.dna)):
            self.check_row(i)
            self.check_letter(i, 0)
            self.consecutive_letters = 0
            for j in range(0, len(self.dna) - 1):
                self.check_letter(i, j + 1)
                self.scan_position(i, j, i, j + 1)
                j += 1
            i += 1

    def scan_columns(self):
        """Scans columns."""

        j = 0
        while (not self.min_sequences_reached() and j < len(self.dna)):
            i = 0
            self.consecutive_letters = 0
            while (not self.min_sequences_reached() and self.continue_scan(len(self.dna) - i)):
                self.scan_position(i, j, i + 1, j)
                i += 1
            j += 1

    def scan_up_foward_diagonals(self):
        """Scans Up Foward Diagonals."""

        row = self.sequence_length - 1
        while (not self.min_sequences_reached() and row < len(self.dna)):
            i = row
            j = 0
            while (not self.min_sequences_reached() and self.continue_scan((row + 1) - j)):
                self.scan_position(i, j, i - 1, j + 1)
                i -= 1
                j += 1
            row += 1
        column = 1

        while (not self.min_sequences_reached() and column < (len(self.dna) - self.sequence_length + 1)):
            i = len(self.dna) - 1
            j = column
            while (not self.min_sequences_reached() and self.continue_scan(len(self.dna) - j)):
                self.scan_position(i, j, i - 1, j + 1)
                i -= 1
                j += 1
            column += 1

    def scan_down_foward_diagonals(self):
        """Scans Down Foward Diagonals."""

        row = len(self.dna) - self.sequence_length
        while (not self.min_sequences_reached() and row >= 0):
            i = row
            j = 0
            while (not self.min_sequences_reached() and self.continue_scan((len(self.dna) - row) - j)):
                self.scan_position(i, j, i + 1, j + 1)
                i += 1
                j += 1
            row -= 1
        column = 1

        while (not self.min_sequences_reached() and column < (len(self.dna) - self.sequence_length + 1)):
            i = 0
            j = column
            while (not self.min_sequences_reached() and self.continue_scan((len(self.dna) - column) - i)):
                self.scan_position(i, j, i + 1, j + 1)
                i += 1
                j += 1
            column += 1
            
    def continue_scan(self, remaining_positions):
        """Verifies if continue scan."""

        continue_scan = False
        if remaining_positions >= (self.sequence_length - self.consecutive_letters):
            continue_scan = True
        return continue_scan

    def scan_position(self, i, j, next_i, next_j):
        """Scans position."""

        current_char = self.dna[i][j]
        next_char = self.dna[next_i][next_j]
        if current_char == next_char:
            self.consecutive_letters += 1
        else:
            self.consecutive_letters = 0
        if self.consecutive_letters == self.sequence_length - 1:
            self.founded_sequences += 1
            self.consecutive_letters = 0

    def min_sequences_reached(self):
        """Verifies if min sequences is reached."""

        sequences_reached = False
        if self.founded_sequences >= self.min_sequence_match:
            sequences_reached = True
        return sequences_reached

    def check_row(self, i):
        """Checks if row len is valid."""

        if len(self.dna[i]) != len(self.dna):
            raise ValueError("Table must be NxN")

    def check_letter(self, i, j):
        """Checks if valid DNA letter."""

        c = self.dna[i][j]
        if c not in self.valid_letters:
            raise ValueError(f"Invalid Character '{c}' at position [{j},{i}]")
