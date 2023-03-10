import json

from decouple import config
from kafka import KafkaProducer


class OrderProducer:
    __producer = None

    @classmethod
    def get_producer(cls) -> KafkaProducer:
        if cls.__producer is None:
            producer_config = {
                "bootstrap_servers": "localhost:29092",
                "client_id": config("KAFKA_CLIENT_ID")
            }

            cls.__producer = KafkaProducer(**producer_config)

        return cls.__producer
