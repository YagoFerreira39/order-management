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

        return order

    @classmethod
    def delete_product_by_id(cls, pk: str):
        return OrderModel.delete(pk)

    @classmethod
    def __order_completed(cls, order: OrderModel):
        order.status = 'completed'
        order.save()
        RedisInfrastructure.get_redis_connection().xadd('order_completed', order.dict(), '*')
