from domain.entity.entity import User
from gateways.connection import session
from gateways.database import save


def create_user(name, email, password):
    user = User(name=name, email=email, password=password)
    save(user)


def read_all_users():
    return session.query(User).all()


def read_active_users():
    return session.query(User).filter(User.active).all()


def read_user_by_email(email):
    return session.query(User).filter(User.email == email).first()


def read_password_by_email(email):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return user.password
    return None



def read_user_by_id(user_id):
    return session.query(User).filter(User.id == user_id).first()


def update_user(user_id, **kwargs):
    user = session.query(User).get(user_id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    session.commit()


def delete_user(user_id):
    user = session.query(User).get(user_id)
    user.active = False
    session.commit()
