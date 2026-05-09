from fastapi.security import OAuth2PasswordBearer 
from app.core.security import verify_token
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.users import User



oauth2scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token = Depends(oauth2scheme),db:Session=Depends(get_db)):

    try:
        payload = verify_token(token) 

    except Exception:
        raise HTTPException(status_code =401, detail="Invalid token")

    user_id = payload.get("user_id") 

    user = db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    return user





