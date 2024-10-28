from typing import List

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel


class YOLO(BaseModel):
    object_id: int
    type: str
    coordinates: List


class ROI(BaseModel):
    yolo: List[YOLO]


class ImageModel(Document):
    project_name: str = None
    project_id: Indexed(str, index_type=pymongo.TEXT)
    image_name: str = None
    image_id: str = None
    roi: ROI = None

    class Settings:
        name = "annotations"
