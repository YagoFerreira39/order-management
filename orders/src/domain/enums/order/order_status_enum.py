from enum import Enum


class OrderStatusEnum(Enum):
    pending = "pending"
    completed = "completed"
    refunded = "refunded"
