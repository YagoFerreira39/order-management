from typing import TypedDict


class OrderDTO(TypedDict):
    unique_id: str
    product_id: str
    account_id: str
    price: float
    fee: float
    total_price: float
    quantity: int
    status: str  # pending, completed, refunded
    type: str
    market: str
    region: str