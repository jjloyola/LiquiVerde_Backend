from typing import Optional
from pydantic import BaseModel


class UpdateItemRequestDto(BaseModel):  # pyright: ignore[reportUndefinedVariable]
    quantity: Optional[int] = None
    priority: Optional[int] = None
    notes: Optional[str] = None