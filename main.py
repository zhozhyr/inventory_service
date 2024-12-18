from fastapi import FastAPI

import crud
from database import database, engine, metadata
from fastapi import APIRouter, HTTPException, Depends
from typing import List
import schemas

app = FastAPI()

metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    await database.connect()


# Получение списка оборудования с пагинацией
@app.get("/", response_model=List[schemas.Equipment])
async def read_equipment(skip: int = 0, limit: int = 10):
    return await crud.get_all_equipment(skip=skip, limit=limit)


# Получение информации об одном оборудовании
@app.get("/{equipment_id}", response_model=schemas.Equipment)
async def read_equipment_by_id(equipment_id: int):
    equipment = await crud.get_equipment(equipment_id)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment


# Создание нового оборудования
@app.post("/", response_model=schemas.Equipment)
async def create_equipment(item: schemas.EquipmentCreate):
    try:
        return await crud.create_equipment(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")

# Обновление оборудования
@app.put("/{equipment_id}", response_model=schemas.Equipment)
async def update_equipment(equipment_id: int, item: schemas.EquipmentUpdate):
    equipment = await crud.update_equipment(equipment_id, item)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
