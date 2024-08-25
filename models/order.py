from pydantic import BaseModel

class Order(BaseModel):
    item_name: str
    quantity: int
    price: float
    customer_name: str
    customer_email: str
    customer_phone: str