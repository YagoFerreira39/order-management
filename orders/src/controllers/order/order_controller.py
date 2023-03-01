from src.domain.types.order_input import OrderInput
from src.services.order.order_service import OrderService


class OrderController:
    __order_service = OrderService

    @classmethod
    def get_all_orders(cls):
        result = cls.__order_service.get_all_orders()
        return result

    @classmethod
    def get_order_by_id(cls, order_id: str):
        result = cls.__order_service.get_order_by_id(order_id)
        return result

    @classmethod
    async def create_order(cls, order_input):
        result = await cls.__order_service.create_order(order=order_input)
        return result

    @classmethod
    async def update_order(cls, order_id, order_updated_data):
        result = await cls.__order_service.update_order_by_id(
            order_id, order_updated_data
        )
        return result

    @classmethod
    def delete_order_by_id(cls, order_id: str):
        result = cls.__order_service.delete_order_by_id(order_id)
