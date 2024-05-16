from pydantic import BaseModel, Field
from typing import Optional

class PropertySchema(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    address: str
    city: str
    state: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class PropertyUpdateSchema(BaseModel):
    property_id: str
    name: str
    address: str
    city: str
    state: str

    class Config:
        orm_mode = True
