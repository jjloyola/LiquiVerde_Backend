from decimal import Decimal
from datetime import datetime
from typing import Optional
from typing_extensions import override
from domains.optimization.shopping_list_optimization_data import ShoppingListOptimizationData
from domains.product_repository_interface import IProductRepository
from domains.shopping_list import ShoppingList
from domains.list_item import ListItem
from domains.shopping_list_repository_interface import IShoppingListRepository
from domains.list_item_repository_interface import IListItemRepository
from domains.shopping_list_service_interface import IShoppingListService



class ShoppingListService(IShoppingListService):
    def __init__(self, shopping_list_repository: IShoppingListRepository, list_item_repository: IListItemRepository, product_repository: IProductRepository):
        self.shopping_list_repository = shopping_list_repository
        self.list_item_repository = list_item_repository
        self.product_repository = product_repository

    @override
    def get_list_by_id(self, list_id: int) -> ShoppingList | None:
        """Get a shopping list by ID"""
        return self.shopping_list_repository.find_by_id(list_id)

    @override
    def create_list(self, name: str, budget_max: Decimal | None = None, currency: str | None = None) -> ShoppingList:
        """Create a new shopping list"""
        return self.shopping_list_repository.save(ShoppingList(
            id=None,
            name=name,
            budget_max=budget_max,
            currency=currency,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ))
    @override
    def add_item_to_list(self, list_id: Optional[int], product_id: int, quantity: int = 1, priority: int = 5, notes: str | None = None) -> ListItem:
        """Add a product to a shopping list"""
        # Verify that the list exists
        if list_id is None:
            #create a new list
            list_id = self.create_list(name="New List").id
        
        shopping_list = self.shopping_list_repository.find_by_id(list_id)
        if not shopping_list:
            raise ValueError(f"Shopping list with id {list_id} not found")
        
        list_item = ListItem(
            id=None,
            list_id=list_id,
            product_id=product_id,
            quantity=quantity,
            priority=priority,
            notes=notes,
            added_at=datetime.now()
        )
        return self.list_item_repository.save(list_item)

    @override
    def delete_list_item(self, list_id: int, item_id: int) -> bool:
        """Delete an item from a shopping list"""
        # Verify that the item exists and belongs to the list
        item_dto = self.list_item_repository.find_by_id(item_id)
        if not item_dto:
            return False
        
        if item_dto.list_id != list_id:
            raise ValueError(f"Item {item_id} does not belong to list {list_id}")
        
        return self.list_item_repository.delete(item_id)

    @override
    def optimize_shopping_list(self, optimization_data: ShoppingListOptimizationData) -> ShoppingListOptimizationData:
        '''optimize the shopping list proposing a new shopping list with the best products and stores to buy them'''
        
        optimization_data.best_solution_shopping_list = optimization_data.original_shopping_list

        product_id = optimization_data.original_shopping_list.products_with_store[0].product_id
        store_id = optimization_data.original_shopping_list.products_with_store[0].store_id
        
        #product_name = optimization_data.original_shopping_list.products_with_store[0].product_name
        #substitute = self.product_repository.find_substitute_by_name_like(product_name)
        
        
        
        
        #returning dummy data for now
        return optimization_data