from pydantic.networks import EmailStr
from sqlmodel import Field, SQLModel


class DioceseBase(SQLModel):
    name: str = Field(index=True, sa_column_kwargs={"unique": True})


class ParishBase(SQLModel):
    name: str = Field(index=True)
    diocese_id: int = Field(default=None, foreign_key="diocese.id")


class ParishionerBase(SQLModel):
    name: str
    email: EmailStr
    parish_id: int = Field(default=None, foreign_key="parish.id")
