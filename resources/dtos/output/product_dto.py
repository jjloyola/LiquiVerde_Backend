from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ProductDTO(BaseModel):
    # Primary key
    id: Optional[int] = None
    
    # Basic product information
    product_name: str = Field(max_length=255)
    barcode: Optional[str] = Field(default=None, max_length=50)
    category: Optional[str] = Field(default=None, max_length=100)
    brand: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    unit: Optional[str] = Field(default=None, max_length=50)
    image_url: Optional[str] = None
    
    # Environmental data
    carbon_footprint: Optional[Decimal] = None
    ecoscore_score: Optional[int] = None
    ecoscore_grade: Optional[str] = Field(default=None, max_length=1)
    
    # Packaging information
    packaging_type: Optional[str] = Field(default=None, max_length=400)
    packaging_materials: Optional[str] = None
    packaging_recyclable: Optional[bool] = None
    
    # Origin information
    origin_country: Optional[str] = Field(default=None, max_length=100)
    countries_tags: Optional[str] = None
    
    # Product flags
    is_fair_trade: bool = False
    is_organic: bool = False
    is_local: bool = False
    
    # Labels and data source
    labels_tags: Optional[str] = None
    data_source: str = Field(default="open_food_facts", max_length=200)
    
    # Scores
    economic_score: Optional[Decimal] = None
    environmental_score: Optional[Decimal] = None
    social_score: Optional[Decimal] = None
    total_score: Optional[Decimal] = None
    
    
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: str,
            datetime: lambda v: v.isoformat()
        }
    )





