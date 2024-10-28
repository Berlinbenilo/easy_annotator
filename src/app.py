from uuid import uuid4

from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from src.api import images, project
from src.entities.od_model import ImageModel
from src.utils.mongo_utils import init_database

app = FastAPI()

app.include_router(images.router)
app.include_router(project.router)


@app.on_event("startup")
async def on_startup():
    await init_database()


@app.get('/')
def home():
    return "API reached"

