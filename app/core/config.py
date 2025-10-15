from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    Mongo_url:str
    Db_name:str
    Alogorithm:str
    Secret_key:str
    Expiry_token:int

    class Config:
        env_file=".env"

settingstructure=Settings()