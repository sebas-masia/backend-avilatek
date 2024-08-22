from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int,  product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(user_id=user_id, state=order.state)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    for item in order.products:
        db_product = db.query(models.Product).filter(
            models.Product.id == item.product_id).first()

        if db_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product with id {item.product_id} not found")

        if db_product.stock < item.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product with id {
                                item.product_id} does not have enough stock. Current stock: {db_product.stock}. Requested quantity: {item.quantity}")

        db_product.stock -= item.quantity
        db.add(db_product)

        db_order_product = models.OrderProduct(
            order_id=db_order.id, product_id=item.product_id, quantity=item.quantity)
        db.add(db_order_product)

    db.commit()
    return db_order


def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Order).filter(models.Order.user_id == user_id).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
