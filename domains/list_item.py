from dataclasses import dataclass
from datetime import datetime

@dataclass
class ListItem:
    id: int | None
    list_id: int
    product_id: int
    quantity: int
    priority: int
    notes: str | None
    added_at: datetime | None

    def to_dict(self):
        """Convert ListItem to dictionary."""
        return {
            "id": self.id,
            "list_id": self.list_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "priority": self.priority,
            "notes": self.notes,
            "added_at": self.added_at.isoformat() if self.added_at else None
        }

    @classmethod
    def from_dict(cls, data: dict):
        if not data:
            return None
        return cls(
            id=data.get("id"),
            list_id=data["list_id"],
            product_id=data["product_id"],
            quantity=data.get("quantity", 1),
            priority=data.get("priority", 5),
            notes=data.get("notes"),
            added_at=data.get("added_at")
        )
