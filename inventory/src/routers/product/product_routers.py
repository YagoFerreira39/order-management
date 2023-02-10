from fastapi import APIRouter, Header

from src.controllers.product.product_controller import ProductController


class ProductRouters:
    __product_router = APIRouter()

    @staticmethod
    def get_product_routers():
        return ProductRouters.__product_router

    @staticmethod
    @__product_router.get("/get_all_products", tags=["Product"])
    def get_all_products():
        products = ProductController.get_all_products()
        return products
