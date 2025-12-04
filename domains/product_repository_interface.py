from domains.product import Product
from abc import ABC, abstractmethod

class IProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        """Save a new product and return it with the generated ID"""
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> Product | None:
        """Find a product by ID"""
        pass

    @abstractmethod
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        pass