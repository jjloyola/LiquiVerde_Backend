from abc import ABC, abstractmethod
from domains.product import ProductWithStore

class IProductService(ABC):
    @abstractmethod
    def get_all_products(self, limit: int) -> list[ProductWithStore]:
        """Get all products"""
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductWithStore | None:
        """Get a product by ID"""
        pass

    @abstractmethod
    def get_by_barcode(self, barcode: str) -> ProductWithStore | None:
        """Get a product by barcode"""
        pass