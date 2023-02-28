import json

from kafka import KafkaProducer


class OrderProducer:
    @staticmethod
    def send_order(topic: str, data):
        order_producer = KafkaProducer(bootstrap_servers="localhost:29092")
        return order_producer.send(topic, json.dumps(data).encode("utf-8"))
