from pathlib import Path
from typing import List
from uuid import uuid4

from fastapi import APIRouter, File, UploadFile, Form

from src.constants.general_properties import static_path
from src.entities.od_model import ImageModel

router = APIRouter(
    prefix="/images",
    tags=["images"]
)


@router.post('/upload/images')
async def upload_images(project_id: str = Form(None), files: List[UploadFile] = File(...)):
    Path(f"{static_path}/uploads").mkdir(exist_ok=True, parents=True)
    for file in files:
        extension = Path(file.filename).suffix
        _id = uuid4()
        # ImageModel(project_name = )
        with open(f"{static_path}/uploads/{_id}", "wb+") as f:
            f.write(file.file.read())
    return {"filenames": [file.filename for file in files]}


@router.get('/upload/{project_id}')
def get_images(project_id: str):
    ...


@router.post('/upload/file/')
def upload_image():
    return {"output": "data"}


@router.delete('/upload/file/')
def delete_images():
    ...


@router.put('/upload')
def update_images():
    ...
