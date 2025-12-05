from datetime import datetime
from sqlmodel import SQLModel, Field

class ProductTable(SQLModel, table=True):
    __tablename__ = "products"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    barcode: str | None = Field(default=None, max_length=50)
    category: str | None = Field(default=None, max_length=100)
    brand: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None)
    unit: str | None = Field(default=None, max_length=50)
    image_url: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)