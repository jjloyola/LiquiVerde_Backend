from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ProductStoreWithPrice:
    store_id:int
    product_id:int
    
    store_name:str
    price:Decimal
    availability:bool
    stock_quantity:int
    
    def to_dict(self):
        return {
            "store_id": self.store_id,
            "product_id": self.product_id,
            "store_name": self.store_name,
            "price": self.price,
            "availability": self.availability,
            "stock_quantity": self.stock_quantity,
        }