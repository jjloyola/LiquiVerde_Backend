from sqlmodel import Session, select
from domains.product import Product
from domains.product_repository_interface import IProductRepository
from infrastructures.database.models import ProductTable

class ProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, product: Product) -> Product:
        """Save a new product and return it with the generated ID"""
        product_table = ProductTable(
            name=product.name,
            barcode=product.barcode,
            category=product.category,
            brand=product.brand,
            description=product.description,
            unit=product.unit,
            image_url=product.image_url
        )
        self.session.add(product_table)
        self.session.commit()
        self.session.refresh(product_table)
        
        return Product(
            id=product_table.id, 
            name=product_table.name,
            barcode=product_table.barcode, 
            category=product_table.category,
            brand=product_table.brand, 
            description=product_table.description, 
            unit=product_table.unit, 
            image_url=product_table.image_url
        )
    
    def find_by_id(self, product_id: int) -> Product | None:
        """Find a product by ID"""
        statement = select(ProductTable).where(ProductTable.id == product_id)
        product_table = self.session.exec(statement).first()
        if not product_table:
            return None
        return Product(
            id=product_table.id, 
            name=product_table.name,
            barcode=product_table.barcode, 
            category=product_table.category,
            brand=product_table.brand, 
            description=product_table.description, 
            unit=product_table.unit, 
            image_url=product_table.image_url
        )
    
    def find_by_barcode(self, barcode: str) -> Product | None:
        """Find a product by barcode"""
        statement = select(ProductTable).where(ProductTable.barcode == barcode)
        product = self.session.exec(statement).first()
        if not product:
                return None
        return Product(
                id=product.id, 
                name=product.name,
                barcode=product.barcode, 
                category=product.category,
                brand=product.brand, 
                description=product.description, 
                unit=product.unit, 
                image_url=product.image_url
            )
    
    def find_by_name_like(self, name: str) -> list[Product]:
        """Find products by name like"""
        statement = select(ProductTable).where(ProductTable.name.like(f"%{name}%"))
        products = self.session.exec(statement).all()
        if not products:
            return []

        products = []
        for product_table in products:
            current_product = Product(
                id=product_table.id, 
                name=product_table.name,
                barcode=product_table.barcode, 
                category=product_table.category,
                brand=product_table.brand, 
                description=product_table.description, 
                unit=product_table.unit, 
                image_url=product_table.image_url
            )
            products.append(current_product)
        return products
    
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        statement = select(ProductTable).limit(limit)
        

        products = self.session.exec(statement).all()
        if not products:
            return []

        products = []
        for p in products:
            current_product = Product(
                id=p.id, 
                name=p.name,  
                barcode=p.barcode, 
                category=p.category,
                brand=p.brand, 
                description=p.description, 
                unit=p.unit, 
                image_url=p.image_url
            )
            products.append(current_product)
        return products