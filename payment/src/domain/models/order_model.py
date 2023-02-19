from redis_om import HashModel

from src.infrastructure.redis.redis_infrastructure import RedisInfrastructure


class OrderModel(HashModel):
    product_id: str
    customer_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Meta:
        database = RedisInfrastructure.get_redis_connection()
