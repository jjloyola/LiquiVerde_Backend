from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ListItemDTO(BaseModel):
    id: Optional[int] = None
    list_id: int
    product_id: int
    quantity: int = Field(default=1)
    priority: int = Field(default=5)
    notes: Optional[str] = None
    added_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
