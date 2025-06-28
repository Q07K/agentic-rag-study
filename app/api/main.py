"""Agentic RAG API Main Application Module"""

from fastapi import FastAPI, HTTPException

from app.api import routers
from app.api.handlers.exception_handler import custom_exception_response
from app.api.handlers.lifespan import lifespan

app = FastAPI(
    title="Agentic RAG API",
    description="API for Agentic RAG",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_exception_handler(
    exc_class_or_status_code=HTTPException,
    handler=custom_exception_response,
)

# Include Router
app.include_router(router=routers.clients.router)
app.include_router(router=routers.vectors.router)
app.include_router(router=routers.collections.router)
