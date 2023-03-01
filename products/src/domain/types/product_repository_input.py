from typing import TypedDict


class ProductRepositoryInput(TypedDict):
    name: str
    quantity: int
    price: float
