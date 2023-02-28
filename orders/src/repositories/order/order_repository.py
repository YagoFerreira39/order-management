import uuid
from json import dumps

from src.domain.models.order_model import OrderModel
from src.domain.types.order_repository_input import OrderRepositoryInput
from src.infrastructure.redis.redis_infrastructure import RedisInfrastructure
from src.repositories.base_repository.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self):
        pass

    @classmethod
    def get_all_orders(cls):
        orders = cls._mongodb_connection.find({}, {"_id": False})
        result = list(orders)

        return result

    @classmethod
    def get_order_by_id(cls, order_id: str):
        order = cls._mongodb_connection.findOne(
            {"unique_id": order_id}, {"_id": False}
        )

        if not order:
            return {"message": "No order found with the given id."}

        return order

    @classmethod
    async def create_order(cls, order: OrderRepositoryInput):
        unique_id = uuid.uuid4()

        new_order = cls._mongodb_connection.insert_one(
            {
                "unique_id": str(unique_id),
                "product_id": order["product_id"],
                "account_id": order["account_id"],
                "price": order["price"],
                "fee": order["fee"],
                "total_price": order["total_price"],
                "quantity": order["quantity"],
                "status": order["status"],
                "type": order["type"],
                "market": order["market"],
                "region": order["region"],
            }
        )

        if not new_order:
            return {"success": False, "message": "Something went wrong."}

        return {"success": True, "message": "Order created with success."}

    @classmethod
    async def update_order_by_id(cls, order_id, order_updated_data):
        response = cls._mongodb_connection.update_one({
            "unique_id": order_id
        }, {
            **order_updated_data
        })

        return response

    @classmethod
    def delete_order_by_id(cls, order_id: str):
        return OrderModel.delete(order_id)

    @classmethod
    def __order_completed(cls, order: OrderModel):
        order.status = "completed"
        order.save()
        RedisInfrastructure.get_redis_connection().xadd(
            "order_completed", order.dict(), "*"
        )
