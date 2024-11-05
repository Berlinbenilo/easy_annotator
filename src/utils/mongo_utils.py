from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.constants.mongo_properties import get_mongo_credentials
from src.entities.od_model import ImageModel, ProjectModel


async def init_database():
    user_name, password, host, port, db_name = get_mongo_credentials()
    client = AsyncIOMotorClient(f"mongodb://{user_name}:{password}@{host}:{port}/{db_name}")
    database = client[db_name]
    await init_beanie(database=database, document_models=[ImageModel, ProjectModel])
