from app.tests.utils import BaseTestCase


class TestMutantRouter(BaseTestCase):
    """Class to manage Mutant router tests."""

    def test_check_mutant(self):
        """Tests muntant endpoint."""

        payload = {
            "dna": ["TAAAAT", "GGCCCC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }
        response = self.client.post("/mutant", json=payload)
        assert response.status_code == 200

    def test_check_no_mutant(self):
        """Tests muntant endpoint no mutant."""

        payload = {
            "dna": ["TAGAAT", "GGCCCT", "TTATGT", "AGAAGG", "CACCTA", "TCACTG"]
        }
        response = self.client.post("/mutant", json=payload)
        assert response.status_code == 403

    def test_invalid_table_size(self):
        """Tests muntant endpoint with invalid table size."""

        payload = {
            "dna": ["TAGAAT", "GGCCCT"]
        }
        response = self.client.post("/mutant", json=payload)
        assert response.status_code == 400
        assert response.json() == {'error': 'Table min length must be 4x4'}

    def test_invalid_row_length(self):
        """Tests muntant endpoint with invalid row length."""

        payload = {
            "dna": ["TAGAAT", "GGCCCT", "TTATGT", "AGAAGG", "CACCTA"]
        }
        response = self.client.post("/mutant", json=payload)
        assert response.status_code == 400
        assert response.json() == {'error': 'Table must be NxN'}

    def test_invalid_letter(self):
        """Tests muntant endpoint with invalid letter."""

        payload = {
            "dna": ["BAAAAT", "GGCCCC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }
        response = self.client.post("/mutant", json=payload)
        assert response.status_code == 400
        assert response.json() == {"error": "Invalid Character 'B' at position [0,0]"}
