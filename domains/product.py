from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    id: int
    product_name: str
    barcode: str
    category: str
    brand: str
    description: str
    unit: str
    image_url: str
    total_score: Decimal | None

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
            "total_score": str(self.total_score) if self.total_score is not None else None
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
            total_score=total_score
        )