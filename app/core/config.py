from pydantic_settings import BaseSettings, SettingsConfigDict 

class Setting(BaseSettings): 

    DATABASE_URL : str 
    SECRET_KEY : str 
    ACCESS_TOKEN_TIME : int 
    ALGORITHM : str 
    LOG_FILE : str 
    LOG_LEVEL : str 
    


    model_config = SettingsConfigDict(env_file =".env")


settings = Setting() 