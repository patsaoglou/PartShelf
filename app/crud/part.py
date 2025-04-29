from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.models.package import Package
from app.models.part import Part
from sqlalchemy.orm import joinedload


def get_part_by_name(db: Session, name: str):
    
    db_part= db.query(Part).filter(Part.name == name).first()
    return db_part
        

def create_part(db: Session, new_part: Part):
    db.add(new_part)
    db.commit()
    db.refresh(new_part)
    return new_part

def get_all_parts(db: Session, limit = 0):
    return db.query(Part).options(
        joinedload(Part.manufacturer),
        joinedload(Part.type),
        joinedload(Part.package),
        joinedload(Part.inventory)
    ).all()