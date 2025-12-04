class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data["id"], name=data["name"], price=data["price"])