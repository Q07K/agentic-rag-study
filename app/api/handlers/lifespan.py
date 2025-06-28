from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.init_sqlite import init_db


def start() -> None:
    """FastAPI startup event"""

    init_db()

    print("service is started.")


def shutdown() -> None:
    """FastAPI shutdown event"""
    print("service is stopped.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # When service starts.
    start()

    yield

    # When service is stopped.
    shutdown()
