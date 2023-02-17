from redis_om import get_redis_connection
from dotenv import load_dotenv
import os

load_dotenv()


class RedisInfrastructure:
    @staticmethod
    def get_redis_connection():
        return get_redis_connection(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            password=os.getenv('REDIS_KEY'),
            decode_responses=True
        )
