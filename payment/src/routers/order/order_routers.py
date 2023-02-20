from fastapi import APIRouter

from src.controllers.order.order_controller import OrderController
from starlette.requests import Request


class OrderRouters:
    __order_router = APIRouter()

    @staticmethod
    def get_order_routers():
        return OrderRouters.__order_router

    @staticmethod
    @__order_router.get("/get_all_orders", tags=["Order"])
    def get_all_orders():
        response = OrderController.get_all_orders()
        return response

    @staticmethod
    @__order_router.post("/create_order", tags=["Order"])
    async def create_order(request: Request):
        body = await request.json()

        order_input = {
            "product_id": body["product_id"],
            "customer_id": body["customer_id"],
            "quantity": body["quantity"]
        }
        print(order_input)
        response = OrderController.create_order(order_input)
        return response
