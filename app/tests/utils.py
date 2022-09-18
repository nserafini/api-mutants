from fastapi.testclient import TestClient

from app.main import app


class BaseTestCase:
    """Base Test Case."""

    app = app
    client = TestClient(app)
