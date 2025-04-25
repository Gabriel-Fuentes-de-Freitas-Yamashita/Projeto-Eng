from pydantic import BaseModel
from typing import List, Optional

class InsumoBase(BaseModel):
    name: str
    quantity: int

class InsumoCreate(InsumoBase):
    restaurant_id: int

class Insumo(InsumoBase):
    id: int
    class Config:
        orm_mode = True

class ReportBase(BaseModel):
    type: str

class ReportCreate(ReportBase):
    restaurant_id: int

class Report(ReportBase):
    id: int
    created_at: Optional[str]
    class Config:
        orm_mode = True

class RestaurantBase(BaseModel):
    name: str
    address: Optional[str] = None

class RestaurantCreate(RestaurantBase):
    owner_id: int

class Restaurant(RestaurantBase):
    id: int
    insumos: List[Insumo] = []
    reports: List[Report] = []
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    restaurants: List[Restaurant] = []
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
