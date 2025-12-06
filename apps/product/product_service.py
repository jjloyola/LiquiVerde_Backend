from domains.product import Product
from domains.product_repository_interface import IProductRepository
from domains.product_service_interface import IProductService

class ProductService(IProductService):
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def get_all_products(self, limit: int) -> list[Product]:
        """Get all products"""
        return self.product_repository.find_all(limit)

    def get_product_by_id(self, product_id: int) -> Product:
        """Get a product by ID"""
        return self.product_repository.find_by_id(product_id)

    def get_by_barcode(self, barcode: str) -> Product | None:
        """Get a product by barcode"""
        return self.product_repository.find_by_barcode(barcode)

    def get_by_name_like(self, text: str) -> list[Product]:
        """Get products by name like"""
        return self.product_repository.find_by_name_like(text)