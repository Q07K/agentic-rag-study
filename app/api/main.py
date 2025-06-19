from fastapi import FastAPI

from app.api import clients, collections, vectors
from app.api.lifespan import lifespan

app = FastAPI(
    title="Agentic RAG API",
    description="API for Agentic RAG",
    version="0.1.0",
    lifespan=lifespan,
)


# Include Router
app.include_router(router=clients.router)
app.include_router(router=vectors.router)
app.include_router(router=collections.router)
