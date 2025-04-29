from db.database import Base
from sqlalchemy import Column, Integer, String

class FileTemplate(Base):
    __tablename__ = "file_templates"

    id = Column(Integer, primary_key=True, index=True)
    template_type = Column(String(255), unique=True, index=True)
    template_name = Column(String(255), unique=True, index=True)
    
    manufacturer_column = Column(String(255), index=True)
    part_name_column =  Column(String(255), index=True)
    package_column = Column(String(255), index=True)
    description_column = Column(String(255), index=True)
    quantity_column = Column(String(255), index=True)