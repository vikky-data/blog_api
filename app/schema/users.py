from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):

    name : str 
    email : EmailStr
    password : str  


class UserResponse(BaseModel):

    id : int 
    name : str 
    email : EmailStr 


    class Config:
        from_attributes = True 

class LoginUser(BaseModel):

    email : EmailStr 
    password : str  





