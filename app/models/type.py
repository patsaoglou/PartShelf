from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.database import Base

class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    part_type = Column(String(255), index=True)
    
    parts = relationship("Part", back_populates="type")
    