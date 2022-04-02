# controllers/parishioners.py
# controllers for parishioners

from fastapi import APIRouter, Depends, HTTPException

from src.models.resources import ParishionerCreate, ParishionerRead
from src.models.tables import Parishioner
from src.services.db import get_session

router = APIRouter(tags=["parishioner"])


def ParishionerNotFound():
    # a bit less overhead than inheriting from HTTPException
    return HTTPException(status_code=404, detail="Parishioner not found")


@router.post("/parishioner/", response_model=ParishionerRead)
def create_parishioner(parishioner: ParishionerCreate, session=Depends(get_session)):
    session.add(parishioner)
    session.commit()
    session.refresh(parishioner)
    return parishioner


@router.get("/parishioner/{parishioner_id}", response_model=ParishionerRead)
def read_parishioner(parishioner_id: int, session=Depends(get_session)):
    parishioner = session.get(Parishioner, parishioner_id)
    if not parishioner:
        raise ParishionerNotFound()
    return parishioner


@router.delete("/parishioner/{parishioner_id}")
def delete_parishioner(parishioner_id: int, session=Depends(get_session)):
    parishioner = session.get(Parishioner, parishioner_id)
    if not parishioner:
        raise ParishionerNotFound()
    session.delete(parishioner)
    session.commit()
    return {"detail": f"Parishioner with ID {parishioner_id} was deleted"}
