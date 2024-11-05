from typing import List, Optional, Dict

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel


class YOLO(BaseModel):
    object_id: int
    type: str
    coordinates: Optional[List[Dict]]


class ROI(BaseModel):
    yolo: List[YOLO]


class SelectiveImage(BaseModel):
    image_id: Optional[str]


class ImageModel(Document):
    project_id: Indexed(str, index_type=pymongo.TEXT)
    image_name: str
    image_id: str
    roi: Optional[ROI] = None

    class Settings:
        name = "annotations"


class ProjectModel(Document):
    project_name: str
    project_id: Indexed(str, index_type=pymongo.TEXT)

    class Settings:
        name = "projects"
