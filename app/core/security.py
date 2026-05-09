from app.core.config import settings 
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError 
from fastapi import HTTPException



def create_token(data:dict):

    encoding = data.copy()

    exp = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_TIME)

    encoding.update({"exp":exp})

    token  = jwt.encode(encoding,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

    return token 


def verify_token(token:str):

    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])

        return payload 
    
    except JWTError:
        raise HTTPException(status_code=401,detail="Expired token") 
    
    except ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Invalid token signature")