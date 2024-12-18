from typing import Optional
from pydantic import BaseModel


class EquipmentBase(BaseModel):
    name: str
    identifier: str
    type: Optional[str]
    location: Optional[str]
    status_id: Optional[int]


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(EquipmentBase):
    pass


class Equipment(EquipmentBase):
    id: int

    class Config:
        orm_mode = True
