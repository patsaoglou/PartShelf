from sqlalchemy import Column, Integer, ForeignKey, String
from db.database import Base
from sqlalchemy.orm import relationship

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    package_type = Column(String(255), index=True)

    parts = relationship("Part", back_populates="package") 