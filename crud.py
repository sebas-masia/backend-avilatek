from sqlalchemy.orm import Session
from models import Product, Order, OrderProduct
from schemas import ProductCreate, Product, OrderCreate, Order, OrderProductCreate, OrderProduct


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int,  product: ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


def create_order(db: Session, order: OrderCreate, user_id: int):
    db_order = Order(user_id=user_id, state=order.state)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    for item in order.products:
        db_order_product = OrderProduct(
            order_id=db_order.id, product_id=item.product_id, quantity=item.quantity)
        db.add(db_order_product)
        db.commit()
    return db_order


def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
