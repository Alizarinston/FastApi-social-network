from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, deps
from app.utils.user import create_any_user

router = APIRouter()


@router.post("/sign-up")
def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate
) -> Any:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system."
        )
    return create_any_user(db, obj_in=user_in)


@router.get("/me")
def read_user_me(
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    return current_user


@router.get("/{user_id}")
def read_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username not exists in the system",
        )
    return user
