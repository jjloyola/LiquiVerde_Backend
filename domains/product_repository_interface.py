from domains.product import ProductWithStore
from abc import ABC, abstractmethod

class IProductRepository(ABC):
    @abstractmethod
    def save(self, product: ProductWithStore) -> ProductWithStore:
        """Save a new product and return it with the generated ID"""
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> ProductWithStore | None:
        """Find a product by ID"""
        pass

    @abstractmethod
    def find_all(self, limit: int) -> list[ProductWithStore]:
        """Get all products"""
        pass

    @abstractmethod
    def find_by_barcode(self, barcode: str) -> ProductWithStore | None:
        """Find a product by barcode"""
        pass
    @abstractmethod
    def find_substitute_by_name_like(self, product_name: str) -> ProductWithStore | None:
        """Find a substitute for a product by name like"""
        pass