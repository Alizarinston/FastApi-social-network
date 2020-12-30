from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, ForeignKey, DateTime, Text, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Post(Base):
    __tablename__ = 'posts'

    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    title = Column(String)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))
    likes = relationship('Like', backref='post', lazy='dynamic')


class Like(Base):
    __tablename__ = 'likes'

    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    is_liked = Column(Boolean, default=True)
