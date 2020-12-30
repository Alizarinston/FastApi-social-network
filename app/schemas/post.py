from datetime import datetime

from pydantic import BaseModel


class PostModel(BaseModel):
    title: str
    content: str
    author_id: int


class PostCreate(BaseModel):
    title: str
    content: str


class PostUpdate(BaseModel):
    content: str


class PostDetailsModel(PostModel):
    """ Return response data """
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
