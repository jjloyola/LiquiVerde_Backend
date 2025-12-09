from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from resources.dtos.output.product_dto import ProductWithStoreDto

class EvaluatedShoppingListDto(BaseModel):
    shopping_list: List[ProductWithStoreDto] = Field( default = [])

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: float,
        }
    )
