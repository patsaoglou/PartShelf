from sqlalchemy.orm import Session
from app.models.package import Package


def get_package_by_name(db: Session, name: str):
    
    db_package = db.query(Package).filter(Package.package_type==name).first()
    return db_package
        

def create_part_package(db: Session, name:str):
    db_package = Package(package_type=name)
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package
    