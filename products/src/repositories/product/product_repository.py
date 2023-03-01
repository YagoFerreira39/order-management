from src.domain.models.product_model import ProductModel
from src.domain.types.product_repository_input import ProductRepositoryInput


def format_product(pk: str):
    product = ProductModel.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


class ProductRepository:
    @classmethod
    def get_all_products(cls):
        products = ProductModel.all_pks()

        return [format_product(pk) for pk in products]

    @classmethod
    def get_product_by_id(cls, pk: str):
        return ProductModel.get(pk)

    @classmethod
    def create_product(cls, product_repository_input: ProductRepositoryInput):

        product = ProductModel(
            name=product_repository_input["name"],
            quantity=product_repository_input["quantity"],
            price=product_repository_input["price"]
        )

        return product.save()

    @classmethod
    async def update_product_quantity_by_product_id(cls, product_id: str, order_quantity: int):
        product_updated = ProductModel.get(product_id)

        if product_updated.quantity < 1:
            return {
                "message": "Product out of stock."
            }

        new_product_quantity = product_updated.quantity - order_quantity

        print("PROD", new_product_quantity)

        data = {"quantity": new_product_quantity}
        product_updated.update(**data)

        return product_updated

    @classmethod
    def delete_product_by_id(cls, pk: str):
        return ProductModel.delete(pk)
