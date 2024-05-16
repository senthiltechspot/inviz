from fastapi import APIRouter, HTTPException
from models import Property, PropertyUpdate
from schemas import PropertySchema
from database import property_collection
from bson import ObjectId
from typing import List

router = APIRouter()

def object_id_converter(property):
    if '_id' in property:
        property['_id'] = str(property['_id'])
    return property

async def fetch_all_properties():
    properties = await property_collection.find().to_list(length=None)
    return [object_id_converter(property) for property in properties]

@router.post("/create_new_property", response_model=List[PropertySchema])
async def create_new_property(property: Property):
    new_property = await property_collection.insert_one(property.dict())
    if new_property.inserted_id:
        return await fetch_all_properties()
    raise HTTPException(status_code=500, detail="Property could not be created")

@router.get("/fetch_property_details", response_model=List[PropertySchema])
async def fetch_property_details(city: str):
    properties = await property_collection.find({"city": city}).to_list(length=None)
    return [object_id_converter(property) for property in properties]

@router.put("/update_property_details", response_model=List[PropertySchema])
async def update_property_details(property: PropertyUpdate):
    if not ObjectId.is_valid(property.property_id):
        raise HTTPException(status_code=400, detail="Invalid property ID")
    
    update_data = {k: v for k, v in property.dict().items() if v is not None and k != "property_id"}
    updated_property = await property_collection.update_one(
        {"_id": ObjectId(property.property_id)}, {"$set": update_data}
    )
    if updated_property.modified_count:
        return await fetch_all_properties()
    raise HTTPException(status_code=500, detail="Property could not be updated")

@router.get("/find_cities_by_state", response_model=List[str])
async def find_cities_by_state(state: str):
    cities = await property_collection.distinct("city", {"state": state})
    return cities

@router.get("/find_similar_properties", response_model=List[PropertySchema])
async def find_similar_properties(property_id: str):
    if not ObjectId.is_valid(property_id):
        raise HTTPException(status_code=400, detail="Invalid property ID")
    
    property = await property_collection.find_one({"_id": ObjectId(property_id)})
    if property:
        city = property.get("city")
        properties = await property_collection.find({"city": city}).to_list(length=None)
        return [object_id_converter(property) for property in properties]
    raise HTTPException(status_code=404, detail="Property not found")
