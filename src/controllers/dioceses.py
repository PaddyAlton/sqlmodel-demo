# controllers/dioceses.py
# controllers for dioceses

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from src.models.resources import DioceseCreate, DioceseRead
from src.models.tables import Diocese

from src.services.db import get_session
from src.services.logs import logger

router = APIRouter(tags=["diocese"])


def DioceseNotFound():
    # a bit less overhead than inheriting from HTTPException
    return HTTPException(status_code=404, detail="Diocese not found")


@router.post("/diocese/", response_model=DioceseRead)
def create_diocese(diocese: DioceseCreate, session=Depends(get_session)):
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


@router.get("/diocese/{diocese_id}", response_model=DioceseRead)
def read_diocese(diocese_id: int, session=Depends(get_session)):
    diocese = session.get(Diocese, diocese_id)
    if not diocese:
        raise DioceseNotFound()
    return diocese


@router.delete("/diocese/{diocese_id}")
def delete_diocese(diocese_id: int, session=Depends(get_session)):
    diocese = session.get(Diocese, diocese_id)
    if not diocese:
        raise DioceseNotFound()
    session.delete(diocese)
    session.commit()
    return {"detail": f"Diocese with ID {diocese_id} was deleted"}
