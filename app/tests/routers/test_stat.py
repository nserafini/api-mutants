from app.tests.utils import BaseTestCase


class TestStatRouter(BaseTestCase):
    """Class to manage Stat router tests."""

    def test_get_stat_endpoint(self):
        """Tests get stat endpoint."""

        response = self.client.get("/stats")
        assert response.status_code == 200
        assert response.json() == {
            'count_mutant_dna': 0,            
            'count_human_dna': 0,
            'ratio': 0
        }
