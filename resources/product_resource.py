from fastapi import APIRouter, HTTPException, Depends
from domains.product_service_interface import IProductService
from dependencies.product_dependencies import get_product_service

product_router = APIRouter(prefix="/products", tags=["products"])

@product_router.get(f"/get_all_products")
def get_all_products(limit: int = 100, product_service: IProductService = Depends(get_product_service)):
    try:
        products = product_service.get_all_products(limit)
        return [product.to_dict() for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))

@product_router.get("/{product_id}")
def get_product_by_id(product_id: int, product_service: IProductService = Depends(get_product_service)):
    try:
        product = product_service.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product.model_dump()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))

@product_router.get("/get_by_barcode/{barcode}")
def get_by_barcode(barcode: str, product_service: IProductService = Depends(get_product_service)):
    try:
        product = product_service.get_by_barcode(barcode)
        if product:
            return product.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))


@product_router.get("/get_by_name_like/{text}")
def get_by_name_like(text: str, product_service: IProductService = Depends(get_product_service)):
    try:
        products = product_service.get_by_name_like(text)
        if products:
            return [product.to_dict() for product in products]
        else:
            raise HTTPException(status_code=404, detail="Products not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))