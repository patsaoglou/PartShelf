from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()

favicon_path = 'favicon.ico'

@router.get("/", response_class=HTMLResponse)
def get_home_template(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/inventory", response_class=HTMLResponse)
def get_inventory_template(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})

@router.get("/component_details", response_class=HTMLResponse)
def get_component_details_template(request: Request):
    return templates.TemplateResponse("component_details.html", {"request": request})

@router.get("/projects", response_class=HTMLResponse)
def get_projects_template(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})