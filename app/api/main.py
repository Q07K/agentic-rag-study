"""Agentic RAG API Main Application Module"""

from fastapi import FastAPI

from app.api import routers
from app.api.handlers.lifespan import lifespan

app = FastAPI(
    title="Agentic RAG API",
    description="API for Agentic RAG",
    version="0.1.0",
    lifespan=lifespan,
)


# Include Router
app.include_router(router=routers.clients.router)
app.include_router(router=routers.vectors.router)
app.include_router(router=routers.collections.router)
