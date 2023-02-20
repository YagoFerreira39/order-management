from fastapi import APIRouter, Header
from starlette.requests import Request
from src.controllers.product.product_controller import ProductController


class ProductRouters:
    __product_router = APIRouter()
    __tags = ["Product"]

    @staticmethod
    def get_product_routers():
        return ProductRouters.__product_router

    @staticmethod
    @__product_router.get("/get_all_products", tags=__tags)
    def get_all_products():
        products = ProductController.get_all_products()
        return products

    @staticmethod
    @__product_router.get("/get_product_by_id/{pk}", tags=__tags)
    def get_product_by_id(pk: str):
        products = ProductController.get_product_by_id(pk)
        return products

    @staticmethod
    @__product_router.post("/create_product", tags=__tags)
    async def create_product(request: Request):
        body = await request.json()

        product_input = {
            "name": body["name"],
            "quantity": body["quantity"],
            "price": body["price"]
        }

        response = ProductController.create_product(product_input)
        return response
