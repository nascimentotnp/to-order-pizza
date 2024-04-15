from domain.entity.entity import PurchaseOrder
from gateways.connection import session


def create_purchase_order(user_id, food_id):
    purchase_order = PurchaseOrder(id_user=user_id, id_food=food_id)
    session.add(purchase_order)
    session.commit()


def read_all_purchase_orders():
    return session.query(PurchaseOrder).all()


def update_purchase_order(purchase_order_id, **kwargs):
    purchase_order = session.query(PurchaseOrder).get(purchase_order_id)
    for key, value in kwargs.items():
        setattr(purchase_order, key, value)
    session.commit()


def delete_purchase_order(purchase_order_id):
    purchase_order = session.query(PurchaseOrder).get(purchase_order_id)
    purchase_order.active = False
    session.commit()
