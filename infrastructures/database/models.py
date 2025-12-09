from datetime import datetime
from decimal import Decimal
from typing import List
from sqlmodel import SQLModel, Field
from sqlmodel import Relationship



class ProductStoresTable(SQLModel, table=True):
    __tablename__ = "product_stores"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)
    
    # Foreign keys
    product_id: int = Field(foreign_key="products.id")
    store_id: int = Field(foreign_key="stores.id")
    price: Decimal = Field(max_digits=10, decimal_places=2)
    currency: str = Field(max_length=3)
    availability: bool = Field(default=True)
    stock_quantity: int = Field(default=0)
    last_updated: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    product: "ProductTable" = Relationship(back_populates="product_stores")
    store: "StoreTable" = Relationship(back_populates="product_stores")
    

class StoreTable(SQLModel, table=True):
    __tablename__ = "stores"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)
    
    # Basic store information
    name: str = Field(max_length=255)
    address: str | None = Field(default=None)
    city: str | None = Field(default=None, max_length=100)
    country: str | None = Field(default=None, max_length=100)
    latitude: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    longitude: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    phone: str | None = Field(default=None, max_length=50)
    website: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    # Direct relationship to junction table (to access price, availability, etc.)
    product_stores: List["ProductStoresTable"] = Relationship(back_populates="store")
    
    # Many-to-many relationship to products (through junction table)
    products: List["ProductTable"] = Relationship(
        link_model=ProductStoresTable,
        sa_relationship_kwargs={
            "primaryjoin": "StoreTable.id == ProductStoresTable.store_id",
            "secondaryjoin": "ProductStoresTable.product_id == ProductTable.id",
            "viewonly": False
        }
    )
    


class ProductTable(SQLModel, table=True):
    __tablename__ = "products"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)
    
    # Basic product information
    product_name: str = Field(max_length=255)
    barcode: str | None = Field(default=None, max_length=50)
    category: str | None = Field(default=None, max_length=100)
    brand: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None)
    unit: str | None = Field(default=None, max_length=50)
    image_url: str | None = Field(default=None)
    
    # Environmental data
    carbon_footprint: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    ecoscore_score: int | None = Field(default=None)
    ecoscore_grade: str | None = Field(default=None, max_length=1)
    
    # Packaging information
    packaging_type: str | None = Field(default=None, max_length=400)
    packaging_materials: str | None = Field(default=None)
    packaging_recyclable: bool | None = Field(default=None)
    
    # Origin information
    origin_country: str | None = Field(default=None, max_length=100)
    countries_tags: str | None = Field(default=None)
    
    # Product flags
    is_fair_trade: bool = Field(default=False)
    is_organic: bool = Field(default=False)
    is_local: bool = Field(default=False)
    
    # Labels and data source
    labels_tags: str | None = Field(default=None)
    data_source: str = Field(default="open_food_facts", max_length=200)
    
    # Scores
    economic_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    environmental_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    social_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    total_score: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    calculated_at: datetime | None = Field(default=None)
    
    # Relationships
    # Direct relationship to junction table (to access price, availability, etc.)
    product_stores: List["ProductStoresTable"] = Relationship(back_populates="product")
    
    # Many-to-many relationship to stores (through junction table)
    stores: List["StoreTable"] = Relationship(
        link_model=ProductStoresTable,
        sa_relationship_kwargs={
            "primaryjoin": "ProductTable.id == ProductStoresTable.product_id",
            "secondaryjoin": "ProductStoresTable.store_id == StoreTable.id",
            "viewonly": False
        }
    )


class ShoppingListsTable(SQLModel, table=True):
    __tablename__ = "shopping_lists"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)

    # Shopping list information
    name: str = Field(max_length=255)
    budget_max: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    currency: str | None = Field(default=None, max_length=3)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default=datetime.now)

class ListItemsTable(SQLModel, table=True):
    __tablename__ = "list_items"
    
    # Primary key
    id: int | None = Field(default=None, primary_key=True)

    #Foreign keys
    list_id: int = Field(foreign_key="shopping_lists.id")
    product_id: int = Field(foreign_key="products.id")
    
    # Item information on the list
    quantity: int = Field(default=1)
    priority: int = Field(default=5)
    notes: str | None = Field(default=None)
    added_at: datetime = Field(default_factory=datetime.now)

    