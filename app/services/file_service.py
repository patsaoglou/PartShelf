import csv
import io
import re
from fastapi import HTTPException, status
import pandas as pd
from sqlalchemy.orm import Session
from app.crud.file_templates import create_file_template, get_available_file_templates, get_template_by_id
from app.models.file_template import FileTemplate
from app.schemas.file_template import FileTemplateAdd, FileTemplateGet
from app.schemas.inventory import PartToInventoryAdd
from app.services.inventory_service import InventoryService

class FileService:
    def add_file_template(db: Session, template: FileTemplateAdd):
        return create_file_template(db ,FileTemplate(
            template_type = template.template_type,
            template_name = template.template_name,
            manufacturer_column = template.manufacturer_column,
            part_name_column =  template.part_name_column,
            package_column = template.package_column,
            description_column = template.description_column,
            quantity_column =template.quantity_column
        ))
    
    def get_available_file_templates(db: Session):
        file_templates = get_available_file_templates(db)
        
        return [
        FileTemplateGet(
            id = template.id,
            template_type = template.template_type,
            template_name = template.template_name,
            
            manufacturer_column = template.manufacturer_column,
            part_name_column = template.part_name_column,
            package_column = template.package_column,
            description_column = template.description_column,
            quantity_column = template.quantity_column,
        )
        for template in file_templates
        ] 
    
    def import_order_csv_file(file_content: bytes, template_id: int, db: Session):
        text_io = io.StringIO(file_content.decode("utf-8"))
        reader = csv.DictReader(text_io)

        file_template = get_template_by_id(db, template_id)
        if not file_template:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Template with id={template_id} not found to parse file"
            )

        for row in reader:
            description = row[file_template.description_column].strip()
            value, part_type = FileService.extract_info(description)
           
            part_to_add = PartToInventoryAdd(
                name = row[file_template.part_name_column].strip(),
                manufacturer = row[file_template.manufacturer_column].strip(),
                package = row[file_template.package_column].strip(),
                quantity = int(row[file_template.quantity_column].strip()),
                description = description,
                part_type = part_type
            )

            InventoryService.add_part_to_inventory(db, part_to_add)

        return text_io

    def extract_info(description):
        if pd.isnull(description):
            return None, None
        
        value_match = re.search(r'\b\d+(?:\.\d+)?\s?(kΩ|Ω|MΩ|nF|uF|pF|F|H|mH|µH)\b', description, re.IGNORECASE)
        value = value_match.group(0) if value_match else ""

        type_match = re.search(r'(Thick Film Resistor|Chip Resistor|Capacitor|Multilayer Ceramic Capacitor|Operational Amplifier)', description, re.IGNORECASE)
        part_type = type_match.group(0) if type_match else ""
        
        return value, part_type
        
