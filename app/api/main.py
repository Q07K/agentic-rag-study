from fastapi import FastAPI

from app.api import client, collections, vector
from app.api.lifespan import lifespan

app = FastAPI(
    title="Agentic RAG API",
    description="API for Agentic RAG",
    version="0.1.0",
    lifespan=lifespan,
)


# Include Router
app.include_router(router=client.router)
app.include_router(router=vector.router)
app.include_router(router=collections.router)
