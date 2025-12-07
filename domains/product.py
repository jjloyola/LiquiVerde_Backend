from dataclasses import dataclass

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
    total_score: int

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "barcode": self.barcode,
            "category": self.category,
            "brand": self.brand,
            "description": self.description,
            "unit": self.unit,
            "image_url": self.image_url,
            "total_score": self.total_score
        } if self else None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data["id"], product_name=data["product_name"], barcode=data["barcode"], category=data["category"], brand=data["brand"], description=data["description"], unit=data["unit"], image_url=data["image_url"], total_score=data["total_score"] ) if data else None