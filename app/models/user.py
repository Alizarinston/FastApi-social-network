from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    posts = relationship('Post', backref='author', lazy='dynamic')
    likes = relationship('Like', backref='user', lazy='dynamic')
