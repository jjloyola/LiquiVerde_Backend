from abc import ABC, abstractmethod
from domains.list_item import ListItem

class IListItemRepository(ABC):
    @abstractmethod
    def save(self, list_item: ListItem) -> ListItem:
        """Save a new list item and return it with the generated ID"""
        pass

    @abstractmethod
    def find_by_id(self, item_id: int) -> ListItem | None:
        """Find a list item by ID"""
        pass

    @abstractmethod
    def find_by_list_id(self, list_id: int) -> list[ListItem]:
        """Find all items in a shopping list"""
        pass

    @abstractmethod
    def update(self, list_item: ListItem) -> ListItem:
        """Update an existing list item"""
        pass

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        """Delete a list item by ID"""
        pass
