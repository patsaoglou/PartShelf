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

class PartInventoryFlatGet(BaseModel):
    id: int
    name: str
    manufacturer: str
    part_type: str
    package: str
    quantity: int

class PartDetailsFlatGet(BaseModel):
    id: int
    name: str
    manufacturer: str
    part_type: str
    package: str
    quantity: int
    description: str