from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PurchaseOrderDTO(BaseModel):
    id: Optional[int]
    id_user: int
    id_food: int
    date: Optional[datetime]
    status: Optional[str]
    active: Optional[bool]

    class Config:
        orm_mode = True
