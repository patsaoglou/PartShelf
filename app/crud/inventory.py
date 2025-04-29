from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.models.part import Part

def get_inventory_by_part_id(db: Session, part_id: int):
    
    db_inventory = db.query(Inventory).filter(Inventory.part_id==part_id).first()
    return db_inventory
        

def create_inventory(db: Session, new_inventory: Inventory):
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory

def update_inventory_quantity(db: Session, inventory:Inventory):
    db.commit()
    db.refresh(inventory)
    return  inventory