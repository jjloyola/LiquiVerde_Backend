from sqlmodel import Session, select
from datetime import datetime
from domains.list_item import ListItem
from domains.list_item_repository_interface import IListItemRepository
from infrastructures.database.models import ListItemsTable

class ListItemRepository(IListItemRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, list_item: ListItem) -> ListItem:
        """Save a new list item and return it with the generated ID"""
        db_item = ListItemsTable(
            list_id=list_item.list_id,
            product_id=list_item.product_id,
            quantity=list_item.quantity,
            priority=list_item.priority,
            notes=list_item.notes,
            added_at=list_item.added_at or datetime.now()
        )
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        
        return ListItem(
            id=db_item.id,
            list_id=db_item.list_id,
            product_id=db_item.product_id,
            quantity=db_item.quantity,
            priority=db_item.priority,
            notes=db_item.notes,
            added_at=db_item.added_at
        )
    
    def find_by_id(self, item_id: int) -> ListItem | None:
        """Find a list item by ID"""
        statement = select(ListItemsTable).where(ListItemsTable.id == item_id)
        try:
            db_item = self.session.exec(statement).first()
        except Exception as e:
            return None
        if not db_item:
            return None
        return ListItem.model_validate(db_item)
    
    def find_by_list_id(self, list_id: int) -> list[ListItem]:
        """Find all items in a shopping list"""
        statement = select(ListItemsTable).where(ListItemsTable.list_id == list_id)
        db_items = self.session.exec(statement).all()
        if not db_items:
            return []

        domain_items = []
        for db_item in db_items:
            current_item = ListItem(
                id=db_item.id,
                list_id=db_item.list_id,
                product_id=db_item.product_id,
                quantity=db_item.quantity,
                priority=db_item.priority,
                notes=db_item.notes,
                added_at=db_item.added_at
            )
            domain_items.append(current_item)
        return domain_items
    
    def update(self, list_item: ListItem) -> ListItem:
        """Update an existing list item"""
        statement = select(ListItemsTable).where(ListItemsTable.id == list_item.id)
        db_item = self.session.exec(statement).first()
        if not db_item:
            raise ValueError(f"List item with id {list_item.id} not found")
        
        db_item.quantity = list_item.quantity
        db_item.priority = list_item.priority
        db_item.notes = list_item.notes
        
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        
        return ListItem(
            id=db_item.id,
            list_id=db_item.list_id,
            product_id=db_item.product_id,
            quantity=db_item.quantity,
            priority=db_item.priority,
            notes=db_item.notes,
            added_at=db_item.added_at
        )
    
    def delete(self, item_id: int) -> bool:
        """Delete a list item by ID"""
        statement = select(ListItemsTable).where(ListItemsTable.id == item_id)
        db_item = self.session.exec(statement).first()
        if not db_item:
            return False
        
        self.session.delete(db_item)
        self.session.commit()
        return True
