import json

from src.domain.extensions.order.order_extensions import OrderExtension
from src.domain.types.order_input import OrderInput
from src.infrastructure.kafka.producers.order_producer import OrderProducer
from src.repositories.order.order_repository import OrderRepository

from decouple import config

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
        topic = config("NEW_ORDER_TOPIC_NAME")

        product_data = cls.__get_product_in_order(order["product_id"])
        formatted_order_model = OrderExtension.to_model(order, product_data)

        response = await cls.__order_repository.create_order(formatted_order_model)

        order_dto = OrderExtension.to_dto(response["result"])

        order_producer = OrderProducer.get_producer()
        order_producer.send(topic=topic, value=json.dumps(order_dto).encode("utf-8"))
        order_producer.flush()

        return response

    @classmethod
    async def update_order_by_id(cls, order_id, order_updated_data):
        response = await cls.__order_repository.update_order_by_id(
            order_id, order_updated_data
        )
        return response

    @classmethod
    def delete_order_by_id(cls, order_id: str):
        response = cls.__order_repository.delete_order_by_id(order_id)
        return response

    @staticmethod
    def __get_product_in_order(product_id: str):
        product_request = requests.get(
            "http://localhost:8000/api/v1/products/get_product_by_id/%s" % product_id
        )
        product_data = product_request.json()
        return product_data
