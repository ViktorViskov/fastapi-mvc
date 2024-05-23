from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# function for enabling CORS on web server
def add(app: FastAPI):
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])