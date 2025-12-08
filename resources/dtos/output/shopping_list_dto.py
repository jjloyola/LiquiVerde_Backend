from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ShoppingListDTO(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=255)
    budget_max: Optional[Decimal] = None
    currency: Optional[str] = Field(default=None, max_length=3)
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            Decimal: str,
            datetime: lambda v: v.isoformat()
        }
    )
