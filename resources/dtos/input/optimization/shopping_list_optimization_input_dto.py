from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field
from resources.dtos.output.product_dto import ProductDto


class ShoppingListOptimizationInputDto(BaseModel):
    price_importance_percentage: float = Field(gt=0)
    sustainability_importance_percentage: float = Field(gt=0)
    budget_max: Decimal = Field(gt=0)

    list_to_optimize: List[ProductDto] = Field(min_length=1)
