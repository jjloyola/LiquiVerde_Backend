from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ProductShortDTO(BaseModel):
    # Primary key
    id: Optional[int] = None
    
    # Basic product information
    barcode: Optional[str] = Field(default=None, max_length=50)
    product_name: str = Field(max_length=255)
    category: Optional[str] = Field(default=None, max_length=100)
    brand: Optional[str] = Field(default=None, max_length=100)
    image_url: Optional[str] = None
    total_score: Optional[Decimal] = None
    
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: str,
        }
    )
