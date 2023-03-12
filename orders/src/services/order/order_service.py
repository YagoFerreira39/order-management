import json
import requests

from typing import NoReturn
from decouple import config

from src.domain.dtos.order.order_dto import OrderDTO
from src.domain.dtos.response.response_dto import ResponseDTO
from src.domain.exceptions.exceptions import FailedRequest, InvalidOrder
from src.domain.extensions.order.order_extensions import OrderExtension
from src.domain.types.order_input import OrderInput
from src.infrastructure.kafka.producers.order_producer import OrderProducer
from src.repositories.order.order_repository import OrderRepository


class OrderService:
    __order_repository = OrderRepository

    @staticmethod
    def get_all_orders():
        response_dto = None

        try:
            orders = OrderRepository.get_all_orders()

            response_dto = ResponseDTO(
                success=True,
                status_code=0,
                message="",
                result=orders
            )

        except FailedRequest:
            response_dto = ResponseDTO(
                success=False,
                status_code=0,
                message="Something went wrong",
                result=None
            )

        finally:
            response = response_dto.get_response_dto()
            return response

    @staticmethod
    def get_order_by_id(order_id: str):
        response_dto = None

        try:
            order = OrderRepository.get_order_by_id(order_id)

            if not order:
                response_dto = ResponseDTO(
                    success=False,
                    status_code=0,
                    message="No order found with the given id.",
                    result=None
                )
            else:
                response_dto = ResponseDTO(
                    success=True,
                    status_code=0,
                    message="",
                    result=order
                )

        except InvalidOrder:
            response_dto = ResponseDTO(
                success=False,
                status_code=0,
                message="No order found with the given id.",
                result=None
            )

        finally:
            response = response_dto.get_response_dto()
            return response

    @staticmethod
    async def create_order(order: OrderInput):
        response_dto = None

        try:
            product_data = OrderService.__get_product_in_order(order["product_id"])
            formatted_order_model = OrderExtension.to_model(order, product_data)

            response = await OrderRepository.create_order(formatted_order_model)

            order_dto = OrderExtension.to_dto(response)

            OrderService.__send_order_to_producer(order_dto)

            response_dto = ResponseDTO(
                success=True,
                status_code=1,
                message="New order created with success.",
                result=None
            )

        except Exception as exception:
            response_dto = ResponseDTO(
                success=False,
                status_code=0,
                message="No order found with the given id.",
                result=None
            )

        finally:
            response = response_dto.get_response_dto()
            return response

    @staticmethod
    async def update_order_by_id(order_id: str, order_updated_data):
        response = await OrderRepository.update_order_by_id(
            order_id, order_updated_data
        )
        return response

    @staticmethod
    def delete_order_by_id(order_id: str):
        response = OrderRepository.delete_order_by_id(order_id)
        return response

    @staticmethod
    def __get_product_in_order(product_id: str):
        product_request = requests.get(
            "http://localhost:8000/api/v1/products/get_product_by_id/%s" % product_id
        )
        product_data = product_request.json()
        return product_data

    @staticmethod
    def __send_order_to_producer(order: OrderDTO) -> NoReturn:
        topic = config("NEW_ORDER_TOPIC_NAME")

        order_producer = OrderProducer.get_producer()
        order_producer.send(topic=topic, value=json.dumps(order).encode("utf-8"))
        order_producer.flush()
