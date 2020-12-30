from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models import Like
from app.schemas.like import LikeCreate, LikeUpdate


class CRUDLike(CRUDBase[Like, LikeCreate, LikeUpdate]):

    def create(self, db: Session, post_id: int, user_id: int, *, obj_in: LikeCreate) -> Like:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['user_id'] = user_id
        obj_in_data['post_id'] = post_id

        return super().create(db, obj_in=obj_in_data)

    def update(self, db: Session, *, db_obj: Like, obj_in: LikeUpdate) -> Like:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)


like = CRUDLike(Like)
