from fastapi import Depends
from sqlmodel import Session
from apps.shopping_list.shopping_list_service import ShoppingListService
from domains.shopping_list_repository_interface import IShoppingListRepository
from domains.list_item_repository_interface import IListItemRepository
from infrastructures.repositories.shopping_list_repository import ShoppingListRepository
from infrastructures.repositories.list_item_repository import ListItemRepository
from infrastructures.database.connection import get_session

def get_shopping_list_repository(session: Session = Depends(get_session)) -> IShoppingListRepository:
    """Create and return ShoppingListRepository instance with database session"""
    return ShoppingListRepository(session)

def get_list_item_repository(session: Session = Depends(get_session)) -> IListItemRepository:
    """Create and return ListItemRepository instance with database session"""
    return ListItemRepository(session)

def get_shopping_list_service(
    shopping_list_repository: IShoppingListRepository = Depends(get_shopping_list_repository),
    list_item_repository: IListItemRepository = Depends(get_list_item_repository)
) -> ShoppingListService:
    """Create and return ShoppingListService instance"""
    return ShoppingListService(shopping_list_repository, list_item_repository)
