from domain.entity.entity import Pizza
from gateways.connection import session


def create_pizza(name, price, filling, size, stuffed_pizza_edge=False, flavor_stuffed_pizza_edge=None):
    pizza = Pizza(name=name, price=price, filling=filling, size=size, stuffed_pizza_edge=stuffed_pizza_edge,
                  flavor_stuffed_pizza_edge=flavor_stuffed_pizza_edge)

    session.add(pizza)
    session.commit()


def read_all_pizzas():
    return session.query(Pizza).all()


def read_active_pizzas():
    return session.query(Pizza).filter(Pizza.active).all()


def read_pizza_by_id(pizza_id):
    return session.query(Pizza).filter(Pizza.id == pizza_id).first()


def update_pizza(pizza_id, **kwargs):
    pizza = session.query(Pizza).get(pizza_id)
    for key, value in kwargs.items():
        setattr(pizza, key, value)
    session.commit()


def delete_pizza(pizza_id):
    pizza = session.query(Pizza).get(pizza_id)
    pizza.active = False
    session.commit()
