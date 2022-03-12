# models/tables.py
# defines SQLModel table models

from pydantic.networks import EmailStr
from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional


class Diocese(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    parishes: List["Parish"] = Relationship(back_populates="diocese")

class Parish(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    diocese_id: int = Field(default=None, foreign_key="diocese.id")
    diocese: Diocese = Relationship(back_populates="parishes")

# class Parishioner(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     email: EmailStr
#     parish: 
