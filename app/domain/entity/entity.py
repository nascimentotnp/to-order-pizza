from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func

from domain.enum.purchase_status import PurchaseStatus
from gateways.database import Base
import bcrypt


class Food(Base):
    __tablename__ = "comida"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    price = Column('price', String(100), nullable=False)
    filling = Column('filling', String(255), nullable=False)
    active = Column('active', Boolean, nullable=False)

    def __init__(self, name, price, filling):
        self.name = name
        self.price = price
        self.filling = filling
        self.active = True


class Pasta(Food):
    __tablename__ = "pasta"

    id = Column('id', Integer, ForeignKey('comida.id'), primary_key=True)
    pasta_type = Column('pasta_type', String(255), nullable=False)
    sauce_type = Column('sauce_type', String(255), nullable=False)

    def __init__(self, name, price, filling, pasta_type, sauce_type):
        super().__init__(name, price, filling)
        self.pasta_type = pasta_type
        self.sauce_type = sauce_type

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'filling': self.filling,
            'pasta_type': self.pasta_type,
            'sauce_type': self.sauce_type
        }


class Pizza(Food):
    __tablename__ = "pizza"

    id = Column('id', Integer, ForeignKey('comida.id'), primary_key=True)
    size = Column('size', String(255), nullable=False)
    stuffed_pizza_edge = Column('edge_stuffed', Boolean)
    flavor_stuffed_pizza_edge = Column('flavor_edge', String(255), nullable=False)

    def __init__(self, name, price, filling, size, stuffed_pizza_edge, flavor_stuffed_pizza_edge):
        super().__init__(name, price, filling)
        self.size = size
        self.stuffed_pizza_edge = stuffed_pizza_edge
        self.flavor_stuffed_pizza_edge = flavor_stuffed_pizza_edge

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'filling': self.filling,
            'size': self.size,
            'stuffed_pizza_edge': self.stuffed_pizza_edge,
            'flavor_stuffed_pizza_edge': self.flavor_stuffed_pizza_edge
        }


class User(Base):
    __tablename__ = "usuario"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(100))
    email = Column('email', String(100))
    password = Column('password', String(100))
    active = Column('active', Boolean, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)
        self.active = True

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'active': self.active
        }


class PurchaseOrder(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_food = Column(Integer, ForeignKey('comida.id'), nullable=False)
    date = Column(DateTime, nullable=False, server_default=func.now())
    status = Column(String, nullable=False, default=PurchaseStatus.WAITING_ACCEPTANCE.value)
    active = Column(Boolean, nullable=False, default=True)

    def __init__(self, id_user, id_food, status=None):
        self.id_user = id_user
        self.id_food = id_food
        self.date = datetime.now()
        self.status = status if status else PurchaseStatus.WAITING_ACCEPTANCE.value
        self.active = True

    def serialize(self):
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_food': self.id_food,
            'date': self.date,
            'status': self.status,
            'active': self.active
        }



