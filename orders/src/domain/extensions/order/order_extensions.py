import uuid

from src.domain.dtos.order.order_dto import OrderDTO
from src.domain.models.order_model import OrderModel
from src.domain.types.order_input import OrderInput


class OrderExtension:
    @staticmethod
    def to_model(order: OrderInput, product: dict) -> OrderModel:
        unique_id = uuid.uuid4()

        order_model = OrderModel(
            unique_id=str(unique_id),
            product_id=order["product_id"],
            price=product["price"],
            fee=0.2 * product["price"],
            total_price=1.5 * product["price"],
            quantity=order["quantity"],
            account_id=order["account_id"],
            status="pending",
            type=order["type"],
            market=order["market"],
            region=order["region"],
        )

        return order_model

    @staticmethod
    def to_dto(order_model: OrderModel) -> OrderDTO:
        order_dto: OrderDTO = {
            "unique_id": order_model["unique_id"],
            "product_id": order_model["product_id"],
            "price": order_model["price"],
            "fee": order_model["price"],
            "total_price": order_model["price"],
            "quantity": order_model["quantity"],
            "account_id": order_model["account_id"],
            "status": order_model["status"],
            "type": order_model["type"],
            "market": order_model["market"],
            "region": order_model["region"]
        }

        return order_dto
