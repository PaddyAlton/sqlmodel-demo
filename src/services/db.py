# services/db.py
# support for connecting to a database and creating the schema

from sqlmodel import Session, SQLModel, create_engine
from src.services.config import AppSettings, get_settings
from typing import Callable


def create_db_and_tables(get_settings: Callable[[], AppSettings]):
    """
    create_db_and_tables

    """
    settings = get_settings()

    connect_args = {"check_same_thread": False}

    # we'll turn off this verbose logging of queries in production:
    echo = settings.application_env != "prod"

    engine = create_engine(
        settings.connection_string, connect_args=connect_args, echo=echo
    )

    SQLModel.metadata.create_all(engine)

    return engine


engine = create_db_and_tables(get_settings)


def get_session():
    with Session(engine) as session:
        yield session
