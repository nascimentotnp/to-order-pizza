from pydantic import BaseModel


class PastaDTO(BaseModel):
    name: str
    price: str
    filling: str
    pasta_type: str
    sauce_type: str
    active: bool = True
