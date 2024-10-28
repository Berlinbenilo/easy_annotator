from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.constants.mongo_properties import get_mongo_credentials
from src.entities.od_model import ImageModel, ROI, YOLO


async def init_database():
    user_name, password, host, port, db_name = get_mongo_credentials()
    client = AsyncIOMotorClient(f"mongodb://{user_name}:{password}@{host}:{port}/{db_name}")
    database = client[db_name]
    await init_beanie(database=database, document_models=[ImageModel])


if __name__ == '__main__':
    import asyncio


    async def insert_dummy_data():
        await init_database()

        dummy_data = ImageModel(
            project_name="Object Detection Project",
            project_id="proj_12345",
            image_name="image_01.jpg",
            image_id="img_12345",
            roi=ROI(
                yolo=[
                    YOLO(object_id=1, type="person", coordinates=[100, 200, 150, 250]),
                    YOLO(object_id=2, type="car", coordinates=[300, 400, 350, 450])
                ]
            )
        )

        await dummy_data.insert()
        inserted_image = await ImageModel.find_one(ImageModel.image_id == "img_12345")
        print(inserted_image)
    asyncio.run(insert_dummy_data())
