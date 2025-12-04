from fastapi import Depends
from apps.product.product_service import ProductService
from domains.product_repository_interface import IProductRepository
from domains.product_service_interface import IProductService
from infrastructures.repositories.product_repository import ProductRepository

def get_product_repository() -> IProductRepository:
    """Create and return ProductRepository instance"""
    return ProductRepository()

def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository)
) -> IProductService:
    """Create and return ProductService instance"""
    return ProductService(product_repository)