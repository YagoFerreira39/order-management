from src.domain.enums.order.order_status_enum import OrderStatusEnum
from src.domain.types.order_input import OrderInput
from src.repositories.order.order_repository import OrderRepository

import requests


class OrderService:
    __order_repository = OrderRepository

    @classmethod
    def get_all_orders(cls):
        response = cls.__order_repository.get_all_orders()
        return response

    @classmethod
    def get_order_by_id(cls, order_id: str):
        response = cls.__order_repository.get_order_by_id(order_id)
        return response

    @classmethod
    async def create_order(cls, order: OrderInput):
        product_data = cls.__get_product_in_order(order["product_id"])
        formatted_order = cls.__format_order(order, product_data)

        response = await cls.__order_repository.create_order(formatted_order)
        return response

    @classmethod
    def delete_product_by_id(cls, pk: str):
        response = cls.__order_repository.delete_product_by_id(pk)
        return response

    @staticmethod
    def __get_product_in_order(product_id: str):
        product_request = requests.get('http://localhost:8000/api/v1/products/get_product_by_id/%s' % product_id)
        product_data = product_request.json()
        return product_data

    @staticmethod
    def __format_order(order, product):
        formatted_order = {
            "product_id": order["product_id"],
            "price": product["price"],
            "fee": 0.2 * product["price"],
            "total": 1.2 * product["price"],
            "quantity": order["quantity"],
            "customer_id": order["customer_id"],
            "status": "pending"
        }
        return formatted_order
