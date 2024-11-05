from uuid import uuid4

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from src.entities.od_model import ProjectModel

router = APIRouter(
    prefix="/project",
    tags=["project"]
)


@router.post('/create')
async def create_project(project_name: str = Form(None)):
    project_id = str(uuid4())
    entities = ProjectModel(project_name=project_name, project_id=project_id)
    await ProjectModel.insert_one(entities)
    return JSONResponse(content={"message": "project created successfully", "project_id": project_id})


@router.put('/update')
async def update_project(project_id: str = Form(), project_name: str = Form()):
    entity = await ProjectModel.find_one(ProjectModel.project_id == project_id)
    if entity is None:
        return JSONResponse(content={"message": "project not found"}, status_code=404)
    await entity.update({"$set": {ProjectModel.project_name: project_name}})
    return JSONResponse(content={"message": "project updated successfully"})


@router.delete('/delete')
async def delete_project(project_id: str = Form()):
    await ProjectModel.find_one(ProjectModel.project_id == project_id).delete()
    return {"message": "Project deleted successfully..!"}


@router.put('/fetch')
async def get_project(project_id: str = Form()):
    result = await ProjectModel.find(ProjectModel.project_id == project_id).to_list()
    return result


@router.get('/fetch_all')
async def get_project():
    projects = await ProjectModel.find({}).to_list()
    return projects
