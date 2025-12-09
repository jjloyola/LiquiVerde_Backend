from dataclasses import dataclass
from decimal import Decimal
from domains.optimization.optimization_product_list_with_store import OptimizationProductListWithStore


@dataclass
class ShoppingListOptimizationData():
    original_shopping_list: OptimizationProductListWithStore
    best_solution_shopping_list: OptimizationProductListWithStore

    @property
    def difference_in_price_vs_best_solution(self) -> Decimal | None:
        if self.best_solution_shopping_list is None or self.original_shopping_list is None:
            return None
        return self.best_solution_shopping_list.total_price - self.original_shopping_list.total_price
    
    @property
    def difference_in_sustainability_score_vs_best_solution(self) -> Decimal | None:
        if self.best_solution_shopping_list is None or self.original_shopping_list is None:
            return None
        return self.best_solution_shopping_list.total_sustainability_score - self.original_shopping_list.total_sustainability_score
    
    @property
    def difference_in_price_score_vs_best_solution(self) -> Decimal | None:
        if self.best_solution_shopping_list is None or self.original_shopping_list is None:
            return None
        return self.best_solution_shopping_list.total_price_score - self.original_shopping_list.total_price_score
    
    @property
    def difference_in_total_score_vs_best_solution(self) -> Decimal | None:
        if self.best_solution_shopping_list is None or self.original_shopping_list is None:
            return None
        return self.best_solution_shopping_list.total_objective_score - self.original_shopping_list.total_objective_score
    

    price_importance_percentage: Decimal 
    sustainability_importance_percentage: Decimal 
    max_budget: Decimal 
