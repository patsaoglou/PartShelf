from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Inventory(Base):
    __tablename__ = "inventories"

    part_id = Column(Integer, ForeignKey("parts.id"), primary_key=True)
    quantity_available = Column(Integer, default=0)

    part = relationship("Part", back_populates="inventory")

