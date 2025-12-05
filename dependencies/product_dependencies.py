from fastapi import Depends
from sqlmodel import Session
from apps.product.product_service import ProductService
from domains.product_repository_interface import IProductRepository
from domains.product_service_interface import IProductService
from infrastructures.repositories.product_repository import ProductRepository
from infrastructures.database.connection import get_session

def get_product_repository(session: Session = Depends(get_session)) -> IProductRepository:
    """Create and return ProductRepository instance with database session"""
    return ProductRepository(session)

def get_product_service(
    product_repository: IProductRepository = Depends(get_product_repository)
) -> ProductService:
    """Create and return ProductService instance"""
    return ProductService(product_repository)