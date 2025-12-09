
from typing_extensions import override
from domains.product import ProductWithStore
from domains.product_repository_interface import IProductRepository
from domains.product_service_interface import IProductService

class ProductService(IProductService):
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    @override
    def get_all_products(self, limit: int) -> list[ProductWithStore]:
        """Get all products"""
        return self.product_repository.find_all(limit)

    @override
    def get_product_by_id(self, product_id: int) -> ProductWithStore | None:
        """Get a product by ID"""
        return self.product_repository.find_by_id(product_id)

    @override
    def get_by_barcode(self, barcode: str) -> ProductWithStore | None:
        """Get a product by barcode"""
        return self.product_repository.find_by_barcode(barcode)

    @override
    def get_by_name_like(self, text: str) -> list[ProductWithStore]:
        """Get products by name like"""
        return self.product_repository.find_by_name_like(text)