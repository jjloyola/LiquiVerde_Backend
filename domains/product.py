from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from pydantic import Field

@dataclass
class Product:
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
    


    

    def to_dict(self):
        """Convert Product to dictionary. Always returns a valid dict."""
        return {
            "id": self.id,
            "product_name": self.product_name,
            "barcode": self.barcode,
            "category": self.category,
            "brand": self.brand,
            "description": self.description,
            "unit": self.unit,
            "image_url": self.image_url,
            "carbon_footprint": self.carbon_footprint,
            "ecoscore_score": self.ecoscore_score,
            "ecoscore_grade": self.ecoscore_grade,
            "packaging_type": self.packaging_type,
            "packaging_materials": self.packaging_materials,
            "packaging_recyclable": self.packaging_recyclable,
            "origin_country": self.origin_country,
            "countries_tags": self.countries_tags,
            "is_fair_trade": self.is_fair_trade,
            "is_organic": self.is_organic,
            "is_local": self.is_local,
            "labels_tags": self.labels_tags,
            "data_source": self.data_source,
            "economic_score": self.economic_score,
            "environmental_score": self.environmental_score,
            "social_score": self.social_score,
            "total_score": str(self.total_score) if self.total_score is not None else None,
        }

    @classmethod
    def from_dict(cls, data: dict):
        if not data:
            return None
        total_score = data.get("total_score")
        if total_score is not None:
            if isinstance(total_score, str):
                total_score = Decimal(total_score)
            elif not isinstance(total_score, Decimal):
                total_score = Decimal(str(total_score))
        return cls(
            id=data["id"], 
            product_name=data["product_name"], 
            barcode=data["barcode"], 
            category=data["category"], 
            brand=data["brand"], 
            description=data["description"], 
            unit=data["unit"], 
            image_url=data["image_url"],
            carbon_footprint=data["carbon_footprint"],
            ecoscore_score=data["ecoscore_score"],
            ecoscore_grade=data["ecoscore_grade"],
            packaging_type=data["packaging_type"],
            packaging_materials=data["packaging_materials"],
            packaging_recyclable=data["packaging_recyclable"],
            origin_country=data["origin_country"],
            countries_tags=data["countries_tags"],
            is_fair_trade=data["is_fair_trade"],
            is_organic=data["is_organic"],
            is_local=data["is_local"],
            labels_tags=data["labels_tags"],
            data_source=data["data_source"],
            economic_score=data["economic_score"],
            environmental_score=data["environmental_score"],
            social_score=data["social_score"],
            total_score=total_score,
        )