from abc import ABC, abstractmethod
from domains.shopping_list import ShoppingList


class IShoppingListRepository(ABC):
    @abstractmethod
    def save(self, shopping_list: ShoppingList) -> ShoppingList:
        """Save a new shopping list and return it with the generated ID"""
        pass

    @abstractmethod
    def find_by_id(self, list_id: int) -> ShoppingList | None:
        """Find a shopping list by ID"""
        pass

    @abstractmethod
    def update(self, shopping_list: ShoppingList) -> ShoppingList:
        """Update an existing shopping list"""
        pass

    @abstractmethod
    def delete(self, list_id: int) -> bool:
        """Delete a shopping list by ID"""
        pass
