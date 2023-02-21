import json

from kafka import KafkaProducer


class OrderProducer:

    __order_producer = KafkaProducer(bootstrap_servers="localhost:29092")

    @classmethod
    def send_order(cls, topic: str, data):
        return cls.__order_producer.send(topic, json.dumps(data).encode("utf-8"))
