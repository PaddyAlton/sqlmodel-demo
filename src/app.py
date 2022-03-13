# app.py
# provides a FastAPI application

from fastapi import FastAPI, Depends
from sqlmodel import Session
from uvicorn import run as serve

from src.controllers import dioceses, parishes, parishioners
from src.models.tables import Diocese, Parish, Parishioner
from src.services.db import get_session
from src.services.config import AppSettings, get_settings
from src.services.logs import logger


app = FastAPI(
    title="My application",
    description="A FastAPI app for demonstrating SQLModel",
    version="0.0.1",
)


@app.on_event("startup")
def check_settings(
    settings: AppSettings = Depends(get_settings), session=Depends(get_session)
):
    logger.info("Application starting. App config was A-Okay.")


@app.get("/")
def root() -> str:
    return f"Welcome to {app.title}!"


# include routers
app.include_router(dioceses.router)
app.include_router(parishes.router)
app.include_router(parishioners.router)


if __name__ == "__main__":

    serve(app, host="0.0.0.0", port=8765)
