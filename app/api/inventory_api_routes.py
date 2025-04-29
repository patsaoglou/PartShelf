from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import RedirectResponse
from app.schemas.file_template import FileTemplateAdd
from app.schemas.inventory import *
from app.services.file_service import FileService
from app.services.inventory_service import *
from db.database import get_db

router = APIRouter()

@router.post("/add_part_to_inventory")
def add_part_to_inventory(
    name: str = Form(...),
    manufacturer: str = Form(...),
    part_type: str = Form(...),
    package: str = Form(...),
    quantity: int = Form(...),
    description: str = Form(None),
    db: Session = Depends(get_db)
):
    
    part_data = PartToInventoryAdd(
        name=name,
        manufacturer=manufacturer,
        part_type=part_type,
        package=package,
        quantity=quantity,
        description=description
    )

    InventoryService.add_part_to_inventory(db, part_data)

    return RedirectResponse("/inventory", status_code=303)

@router.post("/update_quantity")
def update_quantity(update: PartInventoryQuantityUpdate, db: Session = Depends(get_db)):
    return InventoryService.update_inventory_quantity(db, update)

@router.get("/get_parts_inventory")
def get_parts_inventory_list(db: Session = Depends(get_db)):
    return InventoryService.get_parts_inventory_list(db)

@router.post("/add_file_template")
def add_file_template(coloum_template: FileTemplateAdd, db: Session = Depends(get_db)):
    return FileService.add_file_template(db, coloum_template)

@router.get("/get_available_file_templates")
def get_available_file_templates(db: Session = Depends(get_db)):
    return FileService.get_available_file_templates(db)


@router.post("/import_order_csv_file")
async def import_order_csv_file(order_file: UploadFile = File(...), template_id: int = Form(...), db: Session = Depends(get_db)):
    content = await order_file.read()
    result = FileService.import_order_csv_file(content, template_id,db)
    return RedirectResponse("/inventory", status_code=303)