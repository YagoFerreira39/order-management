from typing import List
from src.repositories.product.product_repository import ProductRepository
from src.transport.alpha_vantage.alpha_vantage_transport import AlphaVantageTransport


class ProductService:
    @staticmethod
    async def get_symbol_detail(symbol: str):
        av_symbol: str = symbol + ".sao"

        response = await AlphaVantageTransport().symbol_detail(av_symbol)

        return response

    @staticmethod
    def get_product_by_id(pk: str):
        return ProductRepository.get_product_by_id(pk)

    @staticmethod
    def create_product(product):
        response = ProductRepository.create_product(product)
        return response

    @staticmethod
    async def update_product_quantity_by_product_id(product_id: str, order_quantity: int):
        response = await ProductRepository.update_product_quantity_by_product_id(product_id, order_quantity)
        return response

    @staticmethod
    def delete_product_by_id(pk: str):
        return ProductRepository.delete_product_by_id(pk)
