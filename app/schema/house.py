from pydantic import BaseModel
from typing import Optional


class HouseBase(BaseModel):
    name: str
    city: str
    region: str
    address: str
    is_elevator: bool
    is_trailer: bool
    memo: Optional[str] = None


class HouseSelect(HouseBase):
    id: int
    is_cancel: bool
    skip: int
    limit: int


class HouseCreate(HouseBase):
    pass


class HouseUpdate(HouseBase):
    id: int


class HouseSchema(HouseBase):
    id: int

    class Config:
        from_attributes = True
