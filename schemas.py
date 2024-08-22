from pydantic import BaseModel, EmailStr
from typing import List, Optional


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    password: str
    is_admin: bool

    class Config:
        orm_mode = True


class UserCreate(User):
    username: str
    email: EmailStr
    full_name: str
    password: str
    is_admin: bool = False


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

    class config:
        orm_mode = True


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderProductBase(BaseModel):
    product_id: int
    quantity: int


class OrderProductCreate(OrderProductBase):
    pass


class OrderProduct(OrderProductBase):
    order_id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    state: str = 'pending'
    products: List[OrderProductCreate]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int
    products: List[OrderProduct]

    class Config:
        orm_mode = True
