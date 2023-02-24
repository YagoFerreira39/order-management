from src.domain.models.order_model import OrderModel
from src.domain.types.order_repository_input import OrderRepositoryInput
from src.infrastructure.redis.redis_infrastructure import RedisInfrastructure


class OrderRepository:
    def __init__(self):
        pass

    @classmethod
    def get_all_orders(cls):
        return OrderModel.all_pks()

    @classmethod
    def get_order_by_id(cls, order_id: str):
        return OrderModel.get(order_id)

    @classmethod
    async def create_order(cls, order: OrderRepositoryInput):
        order = OrderModel(
            product_id=order["product_id"],
            customer_id=order["customer_id"],
            price=order["price"],
            fee=order["fee"],
            total=order["total"],
            quantity=order["quantity"],
            status=order["status"]
        )

        order.save()

        return order.dict()

    @classmethod
    async def update_order_by_id(cls, order_id, order_updated_data):
        order_updated = OrderModel.get(order_id)

        print("UPDATE DATA", order_updated_data)

        if order_updated.status == "completed__":
            return {
                "message": "Order is completed and cannot be update anymore."
            }

        order_updated.update(**order_updated_data)

        return order_updated

    @classmethod
    def delete_order_by_id(cls, order_id: str):
        return OrderModel.delete(order_id)

    @classmethod
    def __order_completed(cls, order: OrderModel):
        order.status = 'completed'
        order.save()
        RedisInfrastructure.get_redis_connection().xadd('order_completed', order.dict(), '*')
