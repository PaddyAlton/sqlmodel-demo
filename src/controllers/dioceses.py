# controllers/dioceses.py
# controllers for dioceses

from fastapi import APIRouter, Depends, HTTPException

from src.models.tables import Diocese
from src.services.db import get_session

router = APIRouter(tags=["diocese"])


@router.post("/diocese/")
def create_parish(diocese: Diocese, session=Depends(get_session)) -> Diocese:
    session.add(diocese)
    session.commit(diocese)
    session.refresh(diocese)
    return diocese

@router.get("/diocese/{diocese_id}")
def read_parish(diocese_id: int, session=Depends(get_session)):
    diocese = session.get(Diocese, diocese_id)
    if not diocese:
        raise HTTPException(status_code=404, detail="Diocese not found")
    return diocese
