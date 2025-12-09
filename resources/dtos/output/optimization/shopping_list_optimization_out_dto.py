from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from resources.dtos.output.product_dto import ProductDto
from resources.dtos.output.optimization.evaluated_shopping_list_dto import EvaluatedShoppingListDto


class ShoppingListOptimizationOutputDto(BaseModel):
    original_shopping_list: EvaluatedShoppingListDto
    optimized_shopping_list: EvaluatedShoppingListDto

    difference_in_price: Decimal = Optional[Decimal]
    difference_in_sustainability_score: Decimal = Optional[Decimal]
    difference_in_total_score: Decimal = Optional[Decimal]


    price_importance_percentage: float 
    sustainability_importance_percentage: float 
    budget_max: Decimal 

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: float,
        }
    )

