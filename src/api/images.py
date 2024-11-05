import os
from pathlib import Path
from typing import List
from uuid import uuid4

from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse

from src.constants.general_properties import static_path
from src.entities.od_model import ImageModel, SelectiveImage

router = APIRouter(
    prefix="/images",
    tags=["images"]
)


@router.post('/upload')
async def upload_images(project_id: str = Form(), files: List[UploadFile] = File(...)):
    Path(f"{static_path}/uploads").mkdir(exist_ok=True, parents=True)
    for file in files:
        _id = uuid4()
        entity = ImageModel(project_id=project_id, image_name=file.filename, image_id=str(_id))
        await ImageModel.insert_one(entity)
        with open(f"{static_path}/uploads/{file.filename}", "wb+") as f:
            f.write(file.file.read())
    return {"message": "Image stored successfully..!"}


@router.get('/fetch_one')
async def get_image(image_id: str = Form()):
    result = await ImageModel.find(ImageModel.image_id == image_id).to_list()
    return result


@router.get('/fetch_all')
async def get_all_images(project_id: str = Form(), page: int = Form(..., gt=0), limit: int = Form(..., gt=0)):
    skip = (page - 1) * limit
    images = await ImageModel.find_many({"project_id": project_id}).skip(skip).limit(limit).project(SelectiveImage).to_list()
    total_images = await ImageModel.find_many({"project_id": project_id}).count()
    total_pages = (total_images + limit - 1) // limit
    return {
        "page": page,
        "limit": limit,
        "total_images": total_images,
        "total_pages": total_pages,
        "images": images
    }


@router.delete('/remove')
async def delete_images(image_id: str = Form()):
    await ImageModel.find_one(ImageModel.image_id == image_id).delete()
    return {"message": "Image deleted successfully..!"}


@router.get("/")
async def image_endpoint(image_id: str = Form()):
    result = await ImageModel.find(ImageModel.image_id == image_id).to_list()
    if result:
        file_path = f"{static_path}uploads/{result[0].image_name}"
        if os.path.exists(file_path):
            return FileResponse(file_path, media_type="image/png", filename=f"{image_id}.png")
    return {"message": "File not found!"}
