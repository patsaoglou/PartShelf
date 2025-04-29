from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api import inventory_api_routes, web_routes
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(web_routes.router, tags=["Web Pages"])
app.include_router(inventory_api_routes.router,prefix="/api/inventory")