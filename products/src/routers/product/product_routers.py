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
    @__product_router.get("/{symbol}", tags=__tags)
    async def get_symbol_detail(symbol: str) -> dict:
        products = await ProductController.get_symbol_detail(symbol)
        return products

    @staticmethod
    @__product_router.get("/{pk}", tags=__tags)
    def get_product_by_id(pk: str):
        products = ProductController.get_product_by_id(pk)
        return products

    @staticmethod
    @__product_router.post("", tags=__tags)
    async def create_product(request: Request):
        body = await request.json()

        product_input = {
            "name": body["name"],
            "quantity": body["quantity"],
            "price": body["price"]
        }

        response = ProductController.create_product(product_input)
        return response

    @staticmethod
    @__product_router.put("/{product_id}", tags=__tags)
    async def update_product_quantity_by_product_id(product_id: str, request: Request):
        body = await request.json()
        print("BODY", body)

        response = await ProductController.update_product_quantity_by_product_id(product_id, body["order_quantity"])
        return response
