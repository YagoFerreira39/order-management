from typing import List
from src.repositories.product.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def get_all_products():
        response = ProductRepository.get_all_products()

        print(response)

        return response

    @staticmethod
    def get_product_by_id(pk: str):
        return ProductRepository.get_product_by_id(pk)

    @staticmethod
    def create_product(product):
        response = ProductRepository.create_product(product)
        return response

    @staticmethod
    def delete_product_by_id(pk: str):
        return ProductRepository.delete_product_by_id(pk)
