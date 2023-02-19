from typing import TypedDict

from src.domain.enums.order.order_status_enum import OrderStatusEnum


class OrderRepositoryInput(TypedDict):
    product_id: str
    customer_id: str
    quantity: int
    price: float
    fee: float
    total: float
    status: OrderStatusEnum
