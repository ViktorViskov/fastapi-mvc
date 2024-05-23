from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def add(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")