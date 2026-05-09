from passlib.context import CryptContext 


pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")


def password_hash(password:str):
    hashed = pwd_context.hash(password)

    return hashed 

def password_verification(plain_password,hashed_password):

    verify_password = pwd_context.verify(plain_password,hashed_password)

    return verify_password 