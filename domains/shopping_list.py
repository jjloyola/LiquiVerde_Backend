from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

@dataclass
class ShoppingList:
    id: int | None
    name: str
    budget_max: Decimal | None
    currency: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def to_dict(self):
        """Convert ShoppingList to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "budget_max": str(self.budget_max) if self.budget_max is not None else None,
            "currency": self.currency,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def from_dict(cls, data: dict):
        if not data:
            return None
        budget_max = data.get("budget_max")
        if budget_max is not None:
            if isinstance(budget_max, str):
                budget_max = Decimal(budget_max)
            elif not isinstance(budget_max, Decimal):
                budget_max = Decimal(str(budget_max))
        return cls(
            id=data.get("id"),
            name=data["name"],
            budget_max=budget_max,
            currency=data.get("currency"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )
