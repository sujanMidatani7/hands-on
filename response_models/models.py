from pydantic import BaseModel
from models.customer import Customer

class loginResponse(BaseModel):
    user_id: int
    user: Customer