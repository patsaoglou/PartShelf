from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class ProjectPart(Base):
    __tablename__ = "project_parts"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))
    quantity_needed = Column(Integer)

    project = relationship("Project", back_populates="parts")
    part = relationship("Part")
