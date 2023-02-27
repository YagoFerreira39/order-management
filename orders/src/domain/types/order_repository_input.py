from typing import TypedDict

from src.domain.enums.order.order_status_enum import OrderStatusEnum


class OrderRepositoryInput(TypedDict):
    unique_id: str
    product_id: str
    account_id: str
    quantity: int
    price: float
    fee: float
    total_price: float
    status: OrderStatusEnum
    type: str
    market: str
    region: str
