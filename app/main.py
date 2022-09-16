from fastapi import FastAPI


def init_app():
    """Initialize app."""

    app = FastAPI(title="api-mutant")
    return app


app = init_app()
