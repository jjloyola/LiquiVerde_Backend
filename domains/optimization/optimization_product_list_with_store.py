from dataclasses import dataclass
from decimal import Decimal
from typing import List

from domains.optimization.optimizatin_product_with_store import OptimizationProductWithStore




@dataclass
class OptimizationProductListWithStore:
    
    products_with_store: List[OptimizationProductWithStore]
    
    price_importance_percentage: Decimal 
    sustainability_importance_percentage: Decimal 
    max_budget: Decimal
    
    @property
    def total_price(self) -> Decimal:
        return sum([product.price * product.quantity for product in self.products_with_store])
    
    @property
    def total_sustainability_score(self) -> Decimal:
        return sum([product.sustainability_score * self.sustainability_importance_percentage for product in self.products_with_store])
    
    @property
    def total_price_score(self) -> Decimal:
        return sum([product.price * product.quantity * self.price_importance_percentage for product in self.products_with_store])
    
    @property
    def total_objective_score(self) -> Decimal:
        return self.total_price_score + self.total_sustainability_score
    
    
    @property
    def is_within_budget(self) -> bool:
        if self.max_budget is None or self.total_price is None:
            return True
        return self.total_price <= self.max_budget
    
    