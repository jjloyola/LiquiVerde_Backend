
from decimal import Decimal
from typing import List
from pydantic import BaseModel, ConfigDict

from resources.dtos.output.product_short_dto import ProductShortDTO


class ProductListSearchResultDTO(BaseModel):
    products: List[ProductShortDTO] = []

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: str,
        }
    )