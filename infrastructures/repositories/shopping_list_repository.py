from sqlmodel import Session, select
from datetime import datetime
from domains.shopping_list import ShoppingList
from domains.shopping_list_repository_interface import IShoppingListRepository
from infrastructures.database.models import ShoppingListsTable

class ShoppingListRepository(IShoppingListRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, shopping_list: ShoppingList) -> ShoppingList:
        """Save a new shopping list and return it with the generated ID"""
        db_list = ShoppingListsTable(
            name=shopping_list.name,
            budget_max=shopping_list.budget_max,
            currency=shopping_list.currency,
            created_at=shopping_list.created_at or datetime.now(),
            updated_at=shopping_list.updated_at or datetime.now()
        )
        self.session.add(db_list)
        self.session.commit()
        self.session.refresh(db_list)
        
        return ShoppingList(
            id=db_list.id,
            name=db_list.name,
            budget_max=db_list.budget_max,
            currency=db_list.currency,
            created_at=db_list.created_at,
            updated_at=db_list.updated_at
        )
    
    def find_by_id(self, list_id: int) -> ShoppingList | None:
        """Find a shopping list by ID"""
        statement = select(ShoppingListsTable).where(ShoppingListsTable.id == list_id)
        try:
            db_list = self.session.exec(statement).first()
        except Exception as e:
            return None
        if not db_list:
            return None
        return ShoppingList.model_validate(db_list)

    
    def update(self, shopping_list: ShoppingList) -> ShoppingList:
        """Update an existing shopping list"""
        statement = select(ShoppingListsTable).where(ShoppingListsTable.id == shopping_list.id)
        db_list = self.session.exec(statement).first()
        if not db_list:
            raise ValueError(f"Shopping list with id {shopping_list.id} not found")
        
        db_list.name = shopping_list.name
        db_list.budget_max = shopping_list.budget_max
        db_list.currency = shopping_list.currency
        db_list.updated_at = datetime.now()
        
        self.session.add(db_list)
        self.session.commit()
        self.session.refresh(db_list)
        
        return ShoppingList(
            id=db_list.id,
            name=db_list.name,
            budget_max=db_list.budget_max,
            currency=db_list.currency,
            created_at=db_list.created_at,
            updated_at=db_list.updated_at
        )
    
    def delete(self, list_id: int) -> bool:
        """Delete a shopping list by ID"""
        statement = select(ShoppingListsTable).where(ShoppingListsTable.id == list_id)
        db_list = self.session.exec(statement).first()
        if not db_list:
            return False
        
        self.session.delete(db_list)
        self.session.commit()
        return True
