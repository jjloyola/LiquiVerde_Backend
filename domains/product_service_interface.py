from abc import ABC, abstractmethod

from domains.product import Product
from resources.dtos.product_get_dto import ProductGetDTO

class IProductService(ABC):
    @abstractmethod
    def get_all_products(self, limit: int) -> list[Product]:
        """Get all products"""
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductGetDTO | None:
        """Get a product by ID"""
        pass

    @abstractmethod
    def get_by_barcode(self, barcode: str) -> Product | None:
        """Get a product by barcode"""
        pass