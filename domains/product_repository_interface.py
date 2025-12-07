from domains.product import Product
from abc import ABC, abstractmethod
from resources.dtos.product_get_dto import ProductGetDTO

class IProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        """Save a new product and return it with the generated ID"""
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> ProductGetDTO | None:
        """Find a product by ID"""
        pass

    @abstractmethod
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        pass

    @abstractmethod
    def find_by_barcode(self, barcode: str) -> Product | None:
        """Find a product by barcode"""
        pass