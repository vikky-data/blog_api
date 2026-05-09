from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.db.base import Base 
from sqlalchemy.orm import relationship
from datetime import datetime

class Post(Base):
    __tablename__="posts_table"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)
    user_id = Column(Integer,ForeignKey("users_table.id"))


    users = relationship("User",back_populates="posts")
    comments = relationship("Comment",back_populates="posts")