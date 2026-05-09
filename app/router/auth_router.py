from sqlalchemy.orm import Session
from app.db.database import get_db 
from fastapi import APIRouter,Depends
from app.models.users import User
from app.dependecies.auth import get_current_user
from app.schema.posts import PostCreate, PostResponse,PostUpdate
from app.schema.users import CreateUser, UserResponse,LoginUser
from app.schema.comments import CommentCreate,CommentResponse
from app.services.auth_service import register_user,login_user,post_creation,get_post,single_post,updating,delete_post,comments


router = APIRouter()

@router.post("/signup",response_model=UserResponse)
def signup_user(data:CreateUser,db:Session=Depends(get_db)):
    return register_user(data,db) 

@router.post("/login")
def login(data:LoginUser,db:Session=Depends(get_db)):
    return login_user(data,db) 

@router.post("/create_post",response_model=PostResponse)
def create_post(data:PostCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return post_creation(data,db,current_user.id)

@router.get("/get_posts")
def users_post(db:Session=Depends(get_db)):
    return get_post(db)


@router.get("/single_post/{post_id}")
def get_post(post_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return single_post(db,post_id,current_user.id) 

@router.patch("/updates/{post_id}")
def update(post_id:int,data:PostUpdate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return updating(db,data,post_id,current_user.id)


@router.delete("/delete_post/{post_id}")
def delete (post_id:int,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return delete_post(db,post_id,current_user.id)

@router.post("/add_comment/{post_id}",response_model=CommentResponse)
def add_comment(post_id:int,data:CommentCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return comments(db,data,post_id,current_user.id)