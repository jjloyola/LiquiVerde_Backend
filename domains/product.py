class Product:
    def __init__(self, id: int, name: str, barcode: str, category: str, brand: str, description: str, unit: str, image_url: str):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.category = category
        self.brand = brand
        self.description = description
        self.unit = unit
        self.image_url = image_url

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "barcode": self.barcode,
            "category": self.category,
            "brand": self.brand,
            "description": self.description,
            "unit": self.unit,
            "image_url": self.image_url
        } if self else None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data["id"], name=data["name"], barcode=data["barcode"], category=data["category"], brand=data["brand"], description=data["description"], unit=data["unit"], image_url=data["image_url"] ) if data else None