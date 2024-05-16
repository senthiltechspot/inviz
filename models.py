from pydantic import BaseModel, Field
from typing import Optional

class Property(BaseModel):
    name: str
    address: str
    city: str
    state: str

class PropertyUpdate(BaseModel):
    property_id: str
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
