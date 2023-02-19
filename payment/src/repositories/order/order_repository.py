import requests
import time
from fastapi.background import BackgroundTasks
from starlette.requests import Request

from src.domain.enums.order.order_status_enum import OrderStatusEnum
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
    def get_order_by_id(cls, pk: str):
        return OrderModel.get(pk)

    @classmethod
    async def create_order(cls, order: OrderRepositoryInput):
        req = requests.get('http://localhost:8000/products/%s' % order['product_id'])
        product = req.json()

        order = OrderModel(
            product_id=order["product_id"],
            price=product["price"],
            fee=0.2 * product["price"],
            total=1.2 * product["price"],
            quantity=order["quantity"],
            status=OrderStatusEnum["pending"]
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
