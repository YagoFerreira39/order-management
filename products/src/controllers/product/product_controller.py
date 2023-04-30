from src.services.product.product_service import ProductService


class ProductController:
    @staticmethod
    async def get_symbol_detail(symbol: str) -> object:
        result = await ProductService.get_symbol_detail(symbol)
        return result

    @staticmethod
    def get_product_by_id(pk: str):
        result = ProductService.get_product_by_id(pk)
        return result

    @staticmethod
    def create_product(product):
        result = ProductService.create_product(product)
        return result

    @staticmethod
    async def update_product_quantity_by_product_id(product_id: str, order_quantity: int):
        result = await ProductService.update_product_quantity_by_product_id(product_id, order_quantity)
        return result

    @staticmethod
    def delete_product_by_id(pk: str):
        result = ProductService.delete_product_by_id(pk)
        return result
