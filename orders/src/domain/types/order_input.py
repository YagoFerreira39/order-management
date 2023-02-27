from typing import TypedDict


class OrderInput(TypedDict):
    product_id: str
    account_id: str
    quantity: int
    type: str
    market: str
    region: str
