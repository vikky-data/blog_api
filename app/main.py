from app.db.base import Base 
from app.db.database import engine 
 

from app.models.users import User 
from app.models.posts import Post 
from app.models.comments import Comment 


Base.metadata.create_all(bind=engine)

from fastapi import FastAPI
from app.router import auth_router


app = FastAPI()  

app.include_router(auth_router.router)


