from fastapi import FastAPI

from src.routers.order.order_routers import OrderRouters


class BaseRouters:
    app_v1 = FastAPI()

    @classmethod
    def _initialize_routes(cls) -> FastAPI:
        order_routers = OrderRouters.get_order_routers()
        BaseRouters.app_v1.include_router(router=order_routers, prefix="/order")

        return BaseRouters.app_v1

    @classmethod
    def initialize_routes(cls) -> FastAPI:
        cls._initialize_routes()

        return cls.app_v1
