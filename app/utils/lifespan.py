from contextlib import asynccontextmanager

from fastapi import FastAPI

# from db import context


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Provides a context manager for managing the lifespan of a FastAPI application.

    Inside the `lifespan` context manager, the `before start` and `before stop`
    comments indicate where the startup and shutdown operations should be
    implemented.
    """
    
    # fx db initialization
    # context.init()
    
    # before start
    yield
    # before stop
