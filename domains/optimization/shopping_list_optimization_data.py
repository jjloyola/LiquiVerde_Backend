from dataclasses import dataclass
from decimal import Decimal
from typing import List

from domains.product import ProductWithStore


@dataclass
class ShoppingListOptimizationData():
    original_shopping_list_ids: list[int]
    optimized_shopping_list: list[ProductWithStore]


    original_shopping_list_total_price: Decimal
    optimized_shopping_list_total_price: Decimal
    
    original_shopping_list_sustainability_score: Decimal
    optimized_shopping_list_sustainability_score: Decimal

    original_shopping_list_price_score: Decimal
    optimized_shopping_list_price_score: Decimal

    original_shopping_list_total_objective_score: Decimal
    optimized_shopping_list_total_objective_score: Decimal
    

    difference_in_price: Decimal
    difference_in_sustainability_score: Decimal
    difference_in_total_score: Decimal


    price_importance_percentage: float 
    sustainability_importance_percentage: float 
    budget_max: Decimal 
