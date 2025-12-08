from typing import Optional
from pydantic import BaseModel


class AddItemRequestDto(BaseModel):
    product_id: int
    quantity: int = 1
    priority: int = 5
    notes: Optional[str] = None