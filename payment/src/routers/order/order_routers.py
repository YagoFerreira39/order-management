from fastapi import APIRouter, Header


class OrderRouters:
    __order_router = APIRouter()

    @staticmethod
    def get_order_routers():
        return OrderRouters.__order_router

    @staticmethod
    @__order_router.get("/get_all_orders", tags=["Order"])
    def get_all_orders():
        return []
