from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field
from resources.dtos.input.optimization.product_with_store_optimization_input_dto import ProductWithStoreOptimizationInputDto


class ShoppingListOptimizationInputDto(BaseModel):
    price_importance_percentage: Decimal = Field(gt=0, default=0.5)
    sustainability_importance_percentage: Decimal = Field(gt=0, default=0.5)
    max_budget: Decimal = Field(gt=0, default=10000)

    list_to_optimize: List[ProductWithStoreOptimizationInputDto] = Field(min_length=1)
