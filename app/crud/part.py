from sqlalchemy.orm import Session
from app.models.package import Package
from app.models.part import Part


def get_part_by_name(db: Session, name: str):
    
    db_part= db.query(Part).filter(Part.name == name).first()
    return db_part
        

def create_part(db: Session, new_part: Part):
    db.add(new_part)
    db.commit()
    db.refresh(new_part)