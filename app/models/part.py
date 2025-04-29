from db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(String(255), nullable=True) 
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    package_id = Column(Integer, ForeignKey("packages.id"))
    type_id = Column(Integer, ForeignKey("types.id"))

    manufacturer = relationship("Manufacturer", back_populates="parts")
    package= relationship("Package", back_populates="parts")
    type = relationship("Type", back_populates="parts")
