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
    @__order_router.get("/get_order_by_id/{order_id}", tags=["Order"])
    def get_order_by_id(order_id: str):
        response = OrderController.get_order_by_id(order_id)
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

        response = await OrderController.create_order(order_input)
        return response

    @staticmethod
    @__order_router.put("/update_order_by_id/{order_id}", tags=["Order"])
    async def update_order(order_id, request: Request):
        body = await request.json()
        print("REQ", body)

        print("BODY", body)

        response = await OrderController.update_order(order_id, body)
        return response

    @staticmethod
    @__order_router.delete("/delete_order_by_id/{order_id}", tags=["Order"])
    def delete_order_by_id(order_id: str):
        response = OrderController.delete_order_by_id(order_id)

        return response
