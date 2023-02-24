import json
import requests

from kafka import KafkaConsumer

ORDER_KAFKA_TOPIC = "new_order_created"

order_consumer = KafkaConsumer(ORDER_KAFKA_TOPIC, bootstrap_servers="localhost:29092")

print("Order Consumer Running...")

while True:
    for order in order_consumer:
        consumed_order = json.loads(order.value.decode())

        print("Order", consumed_order)

        product_update_request = requests.put(
            'http://localhost:8000/api/v1/products/update_product_quantity_by_product_id/%s' % consumed_order["product_id"],
            json.dumps({"order_quantity": consumed_order["quantity"]})
        ).json()

        order_update_request = requests.put(
            'http://localhost:8001/api/v1/order/update_order_by_id/%s' % consumed_order["pk"],
            json.dumps({"status": "completed"})
        ).json()

        print("JSON ORDER", order_update_request)
