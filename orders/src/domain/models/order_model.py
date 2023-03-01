from pydantic import BaseModel

from src.domain.enums.order.order_status_enum import OrderStatusEnum


class OrderModel(BaseModel):
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
