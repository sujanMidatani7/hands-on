from pydantic import BaseModel

class Menuresponse(BaseModel):
    name: str
    price: float
    description: str
    available: bool