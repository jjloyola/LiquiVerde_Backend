from fastapi import APIRouter, HTTPException, Depends
from domains.product_service_interface import IProductService
from dependencies.product_dependencies import get_product_service

product_router = APIRouter(prefix="/products", tags=["products"])

@product_router.get(f"/get_all_products/")
def get_products(limit: int = 100, product_service: IProductService = Depends(get_product_service)):
    try:
        products = product_service.get_all_products(limit)
        return [product.to_dict() for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@product_router.get("/{product_id}")
def get_product_by_id(product_id: int, product_service: IProductService = Depends(get_product_service)):
    try:
        product = product_service.get_product_by_id(product_id)
        return product.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
