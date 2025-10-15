from .core.config import settingstructure
from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient(settingstructure.Mongo_url)
db=client[settingstructure.Db_name]