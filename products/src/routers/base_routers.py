from fastapi import FastAPI

from src.routers.product.product_routers import ProductRouters


class BaseRouters:
    app_v1 = FastAPI()

    @classmethod
    def _initialize_routes(cls) -> FastAPI:
        product_routers = ProductRouters.get_product_routers()
        BaseRouters.app_v1.include_router(router=product_routers, prefix="/products")

        return BaseRouters.app_v1

    @classmethod
    def initialize_routes(cls) -> FastAPI:
        cls._initialize_routes()

        return cls.app_v1
