from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/inventory", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})

@router.get("/projects", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})