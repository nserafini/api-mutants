from fastapi import FastAPI

from app.routers.mutant import mutant_router
from app.routers.stat import stat_router
from app.exceptions import exception_middleware


def init_app():
    """Initialize app."""

    app = FastAPI(title="api-mutants")

    app.include_router(
        mutant_router,
        prefix="/mutant", 
        tags=["Mutants"]
    )
    app.include_router(
        stat_router,
        prefix="/stats", 
        tags=["Stats"]
    )
    app.middleware('http')(exception_middleware)
    return app


app = init_app()
