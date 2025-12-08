from abc import ABC, abstractmethod

from domains.product import Product

class IProductService(ABC):
    @abstractmethod
    def get_all_products(self, limit: int) -> list[Product]:
        """Get all products"""
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product | None:
        """Get a product by ID"""
        pass

    @abstractmethod
    def get_by_barcode(self, barcode: str) -> Product | None:
        """Get a product by barcode"""
        pass