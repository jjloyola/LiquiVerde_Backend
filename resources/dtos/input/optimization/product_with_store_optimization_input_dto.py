from decimal import Decimal
from pydantic import BaseModel


class ProductWithStoreOptimizationInputDto(BaseModel):
    product_id: int
    store_id: int
    quantity: int = 1
    price: Decimal
    sustainability_score: Decimal
    
    