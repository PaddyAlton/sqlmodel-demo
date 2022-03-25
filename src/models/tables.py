# models/tables.py
# defines SQLModel table models

from sqlmodel import Field, Relationship
from typing import List, Optional

from src.models.bases import DioceseBase, ParishBase, ParishionerBase


class Diocese(DioceseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    parishes: List["Parish"] = Relationship(back_populates="diocese")


class Parish(ParishBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    diocese: Diocese = Relationship(back_populates="parishes")
    parishioners: List["Parishioner"] = Relationship(back_populates="parish")


class Parishioner(ParishionerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    parish: Parish = Relationship(back_populates="parishioners")
