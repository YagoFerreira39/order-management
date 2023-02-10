from src.services.product.product_service import ProductService


class ProductController:
    @staticmethod
    def get_all_products():
        result = ProductService.get_all_products()
        return result

    @staticmethod
    def get_product_by_id(pk: str):
        result = ProductService.get_product_by_id(pk)
        return result

    @staticmethod
    def delete_product_by_id(pk: str):
        result = ProductService.delete_product_by_id(pk)
        return result
