from sqlalchemy.orm import declarative_base

from gateways.connection import session

Base = declarative_base()


def save(entity: Base):
    session.add(entity)
    session.commit()


def update(entity: Base):
    session.merge(entity)
    session.commit()


def save_all(entities):
    if not isinstance(entities, list):
        entities = [entities]
    for entity in entities:
        session.add(entity)
    session.commit()
