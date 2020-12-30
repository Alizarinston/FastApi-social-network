from datetime import date
from itertools import groupby

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps
from app.models import Like

router = APIRouter()


@router.get("/")
def analytics(
        db: Session = Depends(deps.get_db), *,
        date_from: date = "2020-01-01",
        date_to: date = "2021-01-01",
):
    likes = (db.query(Like).filter(Like.timestamp.between(date_from, date_to)).all())
    result = {}
    for key, group in groupby(likes, lambda x: x.timestamp.day):
        result.update({likes[0].timestamp.date(): len(likes)})

    return result
