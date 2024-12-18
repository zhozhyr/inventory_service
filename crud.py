from database import database
from models import *
import schemas
from sqlalchemy.sql import insert, update
from sqlalchemy.future import select


async def get_equipment(equipment_id: int):
    # Запрос для получения оборудования по ID
    query = select(equipment.c).where(equipment.c.id == equipment_id)
    eq = await database.fetch_one(query)
    if eq is None:
        return None

    eq_dict = dict(eq)

    # Запрос для получения статуса оборудования
    status_query = select(equipment_status).where(equipment_status.c.id == eq["status_id"])
    eq_status = await database.fetch_one(status_query)

    # Добавление информации о статусе в результат
    eq_dict["status"] = dict(eq_status) if eq_status else None
    return eq_dict


async def get_all_equipment(skip: int = 0, limit: int = 100):
    query = select(equipment).offset(skip).limit(limit)
    results = await database.fetch_all(query)
    return [dict(result) for result in results]


async def create_equipment(data: schemas.EquipmentCreate):
    query = insert(equipment).values(**data.dict())
    equipment_id = await database.execute(query)
    return {**data.dict(), "id": equipment_id}


async def update_equipment(equipment_id: int, data: schemas.EquipmentUpdate):
    query = update(equipment).where(equipment.c.id == equipment_id).values(**data.dict())
    await database.execute(query)
    updated_equipment = await get_equipment(equipment_id)
    return updated_equipment
