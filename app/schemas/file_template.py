from pydantic import BaseModel

class FileTemplateAdd(BaseModel):
    template_type: str
    template_name: str
    
    manufacturer_column: str
    part_name_column: str
    package_column: str
    description_column: str
    quantity_column: str

class FileTemplateGet(BaseModel):
    id: int
    template_type: str
    template_name: str
    
    manufacturer_column: str
    part_name_column: str
    package_column: str
    description_column: str
    quantity_column: str