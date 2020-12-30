from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, deps
from app.models import Like

router = APIRouter()


@router.post("/")
def create_post(
        post_in: schemas.PostCreate,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud.post.create(db, author_id=current_user.id, obj_in=post_in)


@router.get("/list")
def get_list_posts(
        db: Session = Depends(deps.get_db), *,
        skip: int = 0,
):
    return crud.post.get_multi(db, skip=skip)


@router.post("/{post_id}/like_unlike")
def post_like_unlike(
        post_id: int,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    post = crud.post.get(db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="The post does not exist in the system",
        )

    like = db.query(Like).filter(Like.post_id == post_id, Like.user_id == current_user.id).first()
    if not like:
        like = crud.like.create(db, post_id=post_id, user_id=current_user.id, obj_in={})
    else:
        crud.like.update(db, db_obj=like, obj_in={'is_liked': not like.is_liked})

    return crud.like.get(db, id=like.id)
