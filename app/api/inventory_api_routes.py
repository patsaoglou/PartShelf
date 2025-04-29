from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from app.schemas.inventory import *
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
