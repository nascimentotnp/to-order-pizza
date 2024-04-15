from domain.entity.entity import Pasta
from gateways.connection import session


def create_pasta(name, price, filling, pasta_type, sauce_type):
    pasta = Pasta(name=name, price=price, filling=filling, pasta_type=pasta_type, sauce_type=sauce_type)
    session.add(pasta)
    session.commit()


def read_all_pastas():
    return session.query(Pasta).all()


def read_active_pastas():
    return session.query(Pasta).filter(Pasta.active).all()


def read_pasta_by_id(pasta_id):
    return session.query(Pasta).filter(Pasta.id == pasta_id).first()


def update_pasta(pasta_id, **kwargs):
    pasta = session.query(Pasta).get(pasta_id)
    for key, value in kwargs.items():
        setattr(pasta, key, value)
    session.commit()


def delete_pasta(pasta_id):
    pasta = session.query(Pasta).get(pasta_id)
    pasta.active = False
    session.commit()
