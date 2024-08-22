from pydantic import BaseModel
from typing import List, Optional


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


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
