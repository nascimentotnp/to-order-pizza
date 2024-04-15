from pydantic import BaseModel


class PizzaDTO(BaseModel):
    name: str
    price: float
    filling: str
    size: str
    stuffed_pizza_edge: bool = False
    flavor_stuffed_pizza_edge: str = None
    active: bool = True