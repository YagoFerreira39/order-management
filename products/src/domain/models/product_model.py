from redis_om import HashModel, get_redis_connection

from src.infrastructure.redis.redis_infrastructure import RedisInfrastructure


class ProductModel(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = RedisInfrastructure.get_redis_connection()
