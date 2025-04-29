from sqlalchemy.orm import Session
from app.models.package import Package
from app.models.type import Type


def get_type_by_name(db: Session, name: str):
    db_type = db.query(Type).filter(Type.part_type==name).first()
    return db_type
        

def create_part_type(db: Session, name: str):
    db_type = Type(part_type=name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)

    return db_type