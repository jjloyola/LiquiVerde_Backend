from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List
from domains.shopping_list import ShoppingList
from domains.list_item import ListItem
from domains.optimization.shopping_list_optimization_data import ShoppingListOptimizationData


class IShoppingListService(ABC):


    @abstractmethod
    def get_list_by_id(self, list_id: int) -> ShoppingList | None:
        """Get a shopping list by ID"""
        pass


    @abstractmethod
    def add_item_to_list(self, list_id: int, product_id: int, quantity: int = 1, priority: int = 5, notes: str | None = None) -> ListItem:
        """Add a product to a shopping list"""
        pass


    @abstractmethod
    def delete_list_item(self, list_id: int, item_id: int) -> bool:
        """Delete an item from a shopping list"""
        pass

    @abstractmethod
    def optimize_shopping_list(self, optimization_data: ShoppingListOptimizationData) -> ShoppingListOptimizationData:
        """Optimize a shopping list"""
        pass
    