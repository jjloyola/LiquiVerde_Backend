from decimal import Decimal
from dataclasses import dataclass

@dataclass
class OptimizationProductWithStore():
    product_id: int
    store_id: int
    quantity: int 
    price: Decimal
    sustainability_score: Decimal
