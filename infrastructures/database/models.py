from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field

class ProductTable(SQLModel, table=True):
    __tablename__ = "products"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)
    
    # Basic product information
    product_name: str = Field(max_length=255)
    barcode: str | None = Field(default=None, max_length=50)
    category: str | None = Field(default=None, max_length=100)
    brand: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None)
    unit: str | None = Field(default=None, max_length=50)
    image_url: str | None = Field(default=None)
    
    # Environmental data
    carbon_footprint: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    ecoscore_score: int | None = Field(default=None)
    ecoscore_grade: str | None = Field(default=None, max_length=1)
    
    # Packaging information
    packaging_type: str | None = Field(default=None, max_length=400)
    packaging_materials: str | None = Field(default=None)
    packaging_recyclable: bool | None = Field(default=None)
    
    # Origin information
    origin_country: str | None = Field(default=None, max_length=100)
    countries_tags: str | None = Field(default=None)
    
    # Product flags
    is_fair_trade: bool = Field(default=False)
    is_organic: bool = Field(default=False)
    is_local: bool = Field(default=False)
    
    # Labels and data source
    labels_tags: str | None = Field(default=None)
    data_source: str = Field(default="open_food_facts", max_length=200)
    
    # Scores
    economic_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    environmental_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    social_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    total_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    calculated_at: datetime | None = Field(default=None)


