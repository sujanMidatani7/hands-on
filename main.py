from fastapi import FastAPI
from models.customer import Customer
from response_models.models import loginResponse
from models.order import Order
from models.menu import Menu
from user.user import  users
from menu.menuData import total_menu, chef_balance
from response_models.menu import Menuresponse
from user.order import orders
app = FastAPI()

@app.get("/login/")
async def login(user_id: int):
    try:
        return users[user_id-1]
    except IndexError:
        return {"error": "User not found"}

@app.post("/signup/", response_model=loginResponse)
async def signup(user: Customer):
    users.append(user)
    return loginResponse(user_id=len(users), user=user)

@app.post("/order/")
async def order(order: Order):
    orders.append(order)
    return {"message": "Order placed successfully"}

@app.get("/order/")
async def get_order(order_id: int):
    return orders[order_id-1]

@app.put("/UpdateOrder/")
async def update_order():
    return {"message": "Order updated successfully"}

@app.post("/menu/")
async def menu(menu: Menu):
    total_menu.append(menu)
    return Menuresponse(name=menu.name, price=menu.price, description=menu.description, available=menu.available)

@app.get("/menu/")
async def get_menu():
    return {"menu": total_menu}

@app.post("/payment/")
async def payment(ammount: float):
    # chef_balance+=ammount
    return {"message": "Payment successful","chef_balance":chef_balance+ammount}
