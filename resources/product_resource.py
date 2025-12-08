from fastapi import APIRouter, HTTPException, Depends
from domains.product import Product
from domains.product_service_interface import IProductService
from dependencies.product_dependencies import get_product_service
from resources.dtos.output.product_list_search_result_dto import ProductListSearchResultDTO
from resources.dtos.output.product_short_dto import ProductShortDTO

product_router = APIRouter(prefix="/products", tags=["products"])

@product_router.get(f"/get_all_products")
def get_all_products(limit: int = 100, product_service: IProductService = Depends(get_product_service)):
    try:
        products = product_service.get_all_products(limit)
        return [product.to_dict() for product in products if product is not None]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))

@product_router.get("/{product_id}")
def get_product_by_id(product_id: int, product_service: IProductService = Depends(get_product_service)):
    try:
        product_domain = product_service.get_product_by_id(product_id)
        if not product_domain:
            raise HTTPException(status_code=404, detail="Product not found")
        return product_domain.to_dict()
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
        domain_products: list[Product] = product_service.get_by_name_like(text)

        if not domain_products:
            raise HTTPException(status_code=404, detail="Products not found")

        
        products_short_dto: list[ProductShortDTO] = []

        for domain_product in domain_products:
            product_short_dto = ProductShortDTO.model_validate(domain_product.to_dict())
            products_short_dto.append(product_short_dto)
        
        product_list_search_result_dto = ProductListSearchResultDTO(products=products_short_dto)

        return product_list_search_result_dto.model_dump(mode="json")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))