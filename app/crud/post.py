from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models import Post
from app.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    def create(self, db: Session, author_id: int, *, obj_in: PostCreate) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['author_id'] = author_id

        return super().create(db, obj_in=obj_in_data)


post = CRUDPost(Post)
