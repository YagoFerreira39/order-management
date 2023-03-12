from src.domain.types.order_input import OrderInput
from src.services.order.order_service import OrderService


class OrderController:
    @staticmethod
    def get_all_orders():
        result = OrderService.get_all_orders()
        return result

    @staticmethod
    def get_order_by_id(order_id: str):
        result = OrderService.get_order_by_id(order_id)
        return result

    @staticmethod
    async def create_order(order_input):
        result = await OrderService.create_order(order=order_input)
        return result

    @staticmethod
    async def update_order(order_id, order_updated_data):
        result = await OrderService.update_order_by_id(
            order_id, order_updated_data
        )
        return result

    @staticmethod
    def delete_order_by_id(order_id: str):
        result = OrderService.delete_order_by_id(order_id)
