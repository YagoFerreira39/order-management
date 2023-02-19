from src.domain.types.order_input import OrderInput
from src.services.order.order_service import OrderService


class OrderController:
    __order_service = OrderService

    @classmethod
    def get_all_orders(cls):
        result = cls.__order_service.get_all_orders()
        return result

    @classmethod
    def get_order_by_id(cls, pk: str):
        result = cls.__order_service.get_order_by_id(pk)
        return result

    @classmethod
    def create_order(cls, order_input: OrderInput):
        print(order_input)
        result = cls.__order_service.create_order(order=order_input)
        return result
