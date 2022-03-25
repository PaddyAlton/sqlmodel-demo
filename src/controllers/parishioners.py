# controllers/parishioners.py
# controllers for parishioners

from fastapi import APIRouter, Depends, HTTPException

from src.models.resources import ParishionerCreate, ParishionerRead
from src.models.tables import Parishioner
from src.services.db import get_session

router = APIRouter(tags=["parishioner"])


@router.post("/parishioner/", response_model=ParishionerRead)
def create_parishioner(
    parishioner: ParishionerCreate, session=Depends(get_session)
) -> Parishioner:
    session.add(parishioner)
    session.commit()
    session.refresh(parishioner)
    return parishioner


@router.get("/parishioner/{parishioner_id}", response_model=ParishionerRead)
def read_parishioner(parishioner_id: int, session=Depends(get_session)):
    parishioner = session.get(Parishioner, parishioner_id)
    if not parishioner:
        raise HTTPException(status_code=404, detail="Parishioner not found")
    return parishioner
