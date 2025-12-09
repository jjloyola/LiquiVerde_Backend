from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from resources.dtos.input.optimization.product_with_store_optimization_input_dto import ProductWithStoreOptimizationInputDto
from resources.dtos.output.optimization.evaluated_shopping_list_dto import EvaluatedShoppingListDto


class ShoppingListOptimizationOutputDto(BaseModel):
    original_shopping_list: EvaluatedShoppingListDto
    optimized_shopping_list: EvaluatedShoppingListDto

    difference_in_price: Decimal = Optional[Decimal]
    difference_in_sustainability_score: Decimal = Optional[Decimal]
    difference_in_total_score: Decimal = Optional[Decimal]


    price_importance_percentage: Decimal 
    sustainability_importance_percentage: Decimal 
    max_budget: Decimal 

    model_config = ConfigDict( 
        from_attributes=True,
        json_encoders={
            Decimal: float,
        }
    )

