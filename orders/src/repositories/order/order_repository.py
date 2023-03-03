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
        order = cls._mongodb_connection.find_one(
            {"unique_id": order_id}, {"_id": False}
        )

        if not order:
            return {"message": "No order found with the given id."}

        return order

    @classmethod
    async def create_order(cls, order: OrderModel):
        new_order = cls._mongodb_connection.insert_one(
            {
                "unique_id": order.unique_id,
                "product_id": order.product_id,
                "account_id": order.account_id,
                "price": order.price,
                "fee": order.fee,
                "total_price": order.total_price,
                "quantity": order.quantity,
                "status": order.status,
                "type": order.type,
                "market": order.market,
                "region": order.region,
            }
        )

        result = cls._mongodb_connection.find_one({"_id": new_order.inserted_id}, {"_id": False})

        if not new_order:
            return {"success": False, "message": "Something went wrong."}

        return {"success": True, "message": "Order created with success.", "result": result}

    @classmethod
    async def update_order_by_id(cls, order_id, order_updated_data):
        result = cls._mongodb_connection.update_one({
            "unique_id": order_id
        }, {
            "$set": {**order_updated_data}
        })

        if not result:
            return {"success": False, "message": "Something went wrong."}

        return {"success": True, "message": "Order updated with success."}

    @classmethod
    def delete_order_by_id(cls, order_id: str):
        result = cls._mongodb_connection.delete_one({
            "unique_id": order_id
        })

        if not result:
            return {"success": False, "message": "Something went wrong."}

        return {"success": True, "message": "Order deleted with success."}
