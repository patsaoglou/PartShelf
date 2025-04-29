from sqlalchemy.orm import Session
from app.models.file_template import FileTemplate


def create_file_template(db: Session, template: FileTemplate):
    db.add(template)
    db.commit()
    db.refresh(template)
    return template

def get_template_by_id(db: Session, template_id: int):
    file_template = db.query(FileTemplate).filter(FileTemplate.id==template_id).first()
    return file_template

def get_available_file_templates(db: Session):
    file_template = db.query(FileTemplate).all()
    return file_template