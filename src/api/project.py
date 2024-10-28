from uuid import uuid4

from typing import Optional
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.entities.od_model import ImageModel

router = APIRouter(
    prefix="/project",
    tags=["project"]
)


class ImageShortView(BaseModel):
    image_id: Optional[str]


@router.post('/create')
async def create_project(project_name: str = Form(None)):
    entities = ImageModel(project_name=project_name, project_id=str(uuid4()))
    await ImageModel.insert_one(entities)
    return JSONResponse(content={"message": "project created successfully"})


@router.get('/fetch/images')
async def get_all_images(project_id: str = Form(), page: int = Form(..., gt=0), limit: int = Form(..., gt=0)):
    skip = (page - 1) * limit
    images = await ImageModel.find_many({"project_id": project_id}).skip(skip).limit(limit).project(ImageShortView).to_list()
    total_images = await ImageModel.find_many({"project_id": project_id}).count()
    total_pages = (total_images + limit - 1) // limit

    return {
        "page": page,
        "limit": limit,
        "total_images": total_images,
        "total_pages": total_pages,
        "images": images
    }
