# controllers/parishes.py
# controllers for parishes

from fastapi import APIRouter, Depends, HTTPException

from src.models.resources import ParishCreate, ParishRead
from src.models.tables import Parish
from src.services.db import get_session

router = APIRouter(tags=["parish"])


@router.post("/parish/", response_model=ParishRead)
def create_parish(parish: ParishCreate, session=Depends(get_session)):
    session.add(parish)
    session.commit()
    session.refresh(parish)
    return parish


@router.get("/parish/{parish_id}", response_model=ParishRead)
def read_parish(parish_id: int, session=Depends(get_session)):
    parish = session.get(Parish, parish_id)
    if not parish:
        raise HTTPException(status_code=404, detail="Parish not found")
    return parish
