from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.api import images, project
from src.utils.mongo_utils import init_database

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

app.include_router(images.router)
app.include_router(project.router)


@app.on_event("startup")
async def on_startup():
    await init_database()


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
