from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship 
from app.db.base import Base

class User(Base):
    __tablename__="users_table"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String) 

    posts = relationship("Post",back_populates="users")
    comments = relationship("Comment",back_populates="users")




