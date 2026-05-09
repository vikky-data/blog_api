from app.logger import create_logger 
from sqlalchemy.orm import Session 
from app.models.users import User 
from app.models.posts import Post
from app.models.comments import Comment
from fastapi import HTTPException 
from app.core.security import create_token
from app.utils.hashing import password_hash,password_verification
from app.schema.users import CreateUser,LoginUser 
from app.schema.comments import CommentCreate
from app.schema.posts import PostCreate,PostUpdate

logger = create_logger(__name__)

def register_user(data:CreateUser,db:Session):

    logger.info("checking for existing user")
    existing_user = db.query(User).filter(User.email==data.email).first() 

    if existing_user:
        logger.info("Email already registered")

        raise HTTPException(status_code=409,detail="Email already reistered")
    
    new_user = User(
        name = data.name,
        email = data.email,
        password = password_hash(data.password)

    ) 

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info("User Successfully created")

    return new_user 

def login_user(data:LoginUser,db:Session):

    check_user = db.query(User).filter(User.email==data.email).first()

    if not check_user:
        logger.warning("Invalid email") 
        raise HTTPException(status_code=401,detail="Inavlid credentials")
    
    if not password_verification(data.password,check_user.password):
        logger.warning("Invalid password")
        raise HTTPException(status_code=401,detail="Invalid credentials") 
    
    data = {
        "user_id":check_user.id,
        "user_email":check_user.email
    } 

    token = create_token(data)

    return token 


def post_creation(data:PostCreate,db:Session,user_id:int):

    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        logger.warning("User not found")
        raise HTTPException(status_code=404,detail="User not found")
    
    new_post = Post(
        title = data.title,
        content = data.content,
        user_id = user_id

    ) 

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    logger.info("Successfully created a post")

    return new_post 

def get_post(db:Session):
    check_post = db.query(Post).all()

    return check_post


def single_post(db:Session,post_id:int,user_id:int):

    check_post=db.query(Post).filter(Post.id==post_id).first()

    if not check_post:
        raise HTTPException(status_code=404,detail="Post not found")
    
    if check_post.user_id != user_id:
        raise HTTPException(status_code=404,detail="User not found")
    
    return check_post  


def updating(db:Session,data:PostUpdate,post_id:int,user_id:int):
    check_post = db.query(Post).filter(Post.id==post_id).first()

    if not check_post:
        raise HTTPException(status_code=404,detail="Post not found")
    
    if check_post.user_id != user_id:
        raise HTTPException(status_code=404, detail="User not found")
    
    updates = data.dict(exclude_unset=True) 

    for key, value in updates.items():
        setattr(check_post,key,value) 

    db.commit() 
    db.refresh(check_post)

    return check_post 


def delete_post(db:Session,post_id:int,user_id:int):
    check_post = db.query(Post).filter(Post.id==post_id).first()
    
    if not check_post:
        raise HTTPException(status_code=404,detail="post not found")
    
    if check_post.user_id != user_id:
        raise HTTPException(status_code=403,detail="user not found")
    
    db.delete(check_post)
    db.commit()

    return {"message":"successfully deleted"} 

def comments(db:Session,data:CommentCreate,post_id:int,user_id:int):
    
    post = db.query(Post).filter(Post.id==post_id).first()

    if not post:
        raise HTTPException(status_code=404,detail="post not found")
    
    comment = Comment(
        content = data.content,
        post_id = post_id,
        user_id = user_id
    )
    
    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment