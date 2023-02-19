from typing import TypedDict


class OrderInput(TypedDict):
    product_id: str
    customer_id: str
    quantity: int
