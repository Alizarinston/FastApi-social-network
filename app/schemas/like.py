from datetime import datetime

from pydantic import BaseModel


class LikeModel(BaseModel):
    is_liked: bool


class LikeCreate(LikeModel):
    is_liked: bool = True


class LikeUpdate(LikeModel):
    pass


class LikeDetailsModel(LikeModel):
    """ Return response data """
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
