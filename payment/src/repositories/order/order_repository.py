import requests
import time
from fastapi.background import BackgroundTasks
from starlette.requests import Request

from src.domain.models.order_model import OrderModel
from src.infrastructure.redis.redis_infrastructure import RedisInfrastructure


class OrderRepository:
    @classmethod
    def get_all_orders(cls):
        return OrderModel.all_pks()

    @classmethod
    def get(cls, pk: str):
        return OrderModel.get(pk)

    @classmethod
    async def create_order(cls, request: Request, background_tasks: BackgroundTasks):
        body = await request.json()

        req = requests.get('http://localhost:8000/products/%s' % body['id'])
        product = req.json()

        order = OrderModel(
            product_id=body["id"],
            price=product["price"],
            fee=0.2 * product["price"],
            total=1.2 * product["price"],
            quantity=body["quantity"],
            status="pending"
        )

        order.save()

        background_tasks.add_task(cls.__order_completed, order)

        return order

    @classmethod
    def __order_completed(cls, order: OrderModel):
        time.sleep(5)
        order.status = 'completed'
        order.save()
        RedisInfrastructure.get_redis_connection().xadd('order_completed', order.dict(), '*')
