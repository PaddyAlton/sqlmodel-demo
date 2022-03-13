# controllers/dioceses.py
# controllers for dioceses

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from src.models.tables import Diocese
from src.services.db import get_session
from src.services.logs import logger

router = APIRouter(tags=["diocese"])


@router.post("/diocese/")
def create_diocese(diocese: Diocese, session=Depends(get_session)) -> Diocese:
    logger.info("Attempting to create Diocese")
    try:
        session.add(diocese)
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=409, detail="A diocese with this name already exists"
        )
    session.refresh(diocese)
    return diocese


@router.get("/diocese/{diocese_id}")
def read_diocese(diocese_id: int, session=Depends(get_session)):
    diocese = session.get(Diocese, diocese_id)
    if not diocese:
        raise HTTPException(status_code=404, detail="Diocese not found")
    return diocese
