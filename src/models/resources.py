# src/models/create.py
# models for resource creation

from pydantic.networks import EmailStr
from sqlmodel import SQLModel
from typing import List, Optional

from src.models.bases import DioceseBase, ParishBase, ParishionerBase


### DIOCESE RESOURCE MODELS
class DioceseCreate(DioceseBase):
    pass


class DioceseRead(DioceseBase):
    id: int


class DioceseUpdate(SQLModel):
    name: Optional[str]


### PARISH RESOURCE MODELS
class ParishCreate(ParishBase):
    pass


class ParishRead(ParishBase):
    id: int


class ParishUpdate(SQLModel):
    name: Optional[str]
    diocese_id: Optional[int]


### PARISHIONER RESOURCE MODELS
class ParishionerCreate(ParishionerBase):
    pass


class ParishionerRead(ParishionerBase):
    id: int


class ParishionerUpdate(SQLModel):
    name: Optional[str]
    email: Optional[EmailStr]
    parish_id: Optional[int]


### RESOURCE MODELS WITH RELATIONSHIPS
class DioceseReadWithParishes(DioceseRead):
    parishes: List[ParishRead]


class ParishReadWithDiocese(ParishRead):
    diocese: DioceseRead


class ParishReadWithParishioners(ParishRead):
    parishioners: List[ParishionerRead] = []


class ParishReadFull(ParishReadWithDiocese, ParishReadWithParishioners):
    pass


class ParishionerReadWithParish(ParishionerRead):
    parish: ParishRead


class ParishionerReadFull(ParishionerRead):
    parish: ParishReadWithDiocese
