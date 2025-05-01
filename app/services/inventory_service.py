from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.crud.inventory import create_inventory, get_inventory_by_part_id, update_inventory_quantity
from app.crud.manufacturer import *
from app.crud.package import *
from app.crud.part import create_part, get_all_parts, get_part_by_id, get_part_by_name, get_parts_containing_key
from app.crud.type import *
from app.models.part import Part
from app.models.inventory import Inventory
from app.schemas.inventory import PartDetailsFlatGet, PartInventoryFlatGet, PartInventoryQuantity, PartInventoryQuantityUpdate, PartToInventoryAdd


class InventoryService:
    def add_part_to_inventory(db: Session, part: PartToInventoryAdd):
        if part.quantity < 0:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Cannot add new part with negative quantity"
            )


        db_manufacturer = get_manufacturer_by_name(db, part.manufacturer)
        if(not db_manufacturer):
            db_manufacturer = create_manufacturer(db, part.manufacturer)
           
        db_package = get_package_by_name(db, part.package)
        if(not db_package):
            db_package = create_part_package(db, part.package)

        db_type = get_type_by_name(db, part.part_type)
        if(not db_type):
            db_type = create_part_type(db, part.part_type)


        db_part = get_part_by_name(db, part.name)
        if not db_part:
            db_part = create_part(db, Part(
                name=part.name,
                description=part.description,
                manufacturer_id=db_manufacturer.id,
                package_id=db_package.id,
                type_id=db_type.id
                ))
            
        
        
        db_inventory = get_inventory_by_part_id(db, db_part.id)
        if not db_inventory:
            db_inventory = Inventory(
                part_id = db_part.id,
                quantity_available = part.quantity                
            )
            create_inventory(db, db_inventory)            
        else:
            InventoryService.update_inventory_quantity(db, PartInventoryQuantityUpdate(part_id=db_part.id, quantity=part.quantity))
        

        return part

    def update_inventory_quantity(db: Session, inventory_quantity: PartInventoryQuantityUpdate):
        db_inventory = get_inventory_by_part_id(db, inventory_quantity.part_id)
        if not db_inventory:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Inventory record not found."
            )

        new_quantity = db_inventory.quantity_available + inventory_quantity.quantity

        if new_quantity < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock to remove {abs(inventory_quantity.quantity)} items. Available: {db_inventory.quantity_available}"
            )

        db_inventory.quantity_available = new_quantity

        update_inventory_quantity(db, db_inventory)
        
        return PartInventoryQuantity(updatedQuantity = db_inventory.quantity_available)



    def get_parts_inventory_list(db: Session):
        parts_list = get_all_parts(db)
        
        return [
        PartInventoryFlatGet(
            id=part.id,
            name=part.name,
            manufacturer=part.manufacturer.name if part.manufacturer else None,
            part_type=part.type.part_type if part.type else None,
            package=part.package.package_type if part.package else None,
            quantity=part.inventory.quantity_available if part.inventory else None
        )
        for part in parts_list
        ]


    def get_part_by_id(db: Session, id: int):
        part_found = get_part_by_id(db, id)
        if part_found is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Part with id = {id} does not exist"
            )
        
        return PartDetailsFlatGet(
            id=part_found.id,
            name=part_found.name,
            manufacturer=part_found.manufacturer.name if part_found.manufacturer else None,
            part_type=part_found.type.part_type if part_found.type else None,
            package=part_found.package.package_type if part_found.package else None,
            quantity=part_found.inventory.quantity_available if part_found.inventory else None,
            description=part_found.description if part_found.description else None
        )
        

    def search(search_key:str, db: Session):
        parts_list = get_parts_containing_key(db, search_key)
        
        return [
        PartInventoryFlatGet(
            id=part.id,
            name=part.name,
            manufacturer=part.manufacturer.name if part.manufacturer else None,
            part_type=part.type.part_type if part.type else None,
            package=part.package.package_type if part.package else None,
            quantity=part.inventory.quantity_available if part.inventory else None
        )
        for part in parts_list
        ]