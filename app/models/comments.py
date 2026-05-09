from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.db.base import Base
from sqlalchemy.orm import relationship 
from datetime import datetime


class Comment(Base):
    __tablename__="comments_table"


    id = Column(Integer,primary_key=True)
    content = Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)
    user_id = Column(Integer,ForeignKey("users_table.id"))
    post_id = Column(Integer,ForeignKey("posts_table.id"))


    users = relationship("User",back_populates="comments")
    posts = relationship("Post",back_populates="comments")