from pydantic import BaseModel

class PartToInventoryAdd(BaseModel):
    name: str
    manufacturer: str
    part_type: str
    package: str
    quantity: int
    description: str | None = None

class PartInventoryQuantityUpdate(BaseModel):
    part_id: int
    quantity: int

class PartInventoryQuantity(BaseModel):
    updatedQuantity: int