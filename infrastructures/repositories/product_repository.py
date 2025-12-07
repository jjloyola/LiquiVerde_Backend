from sqlmodel import Session, select
from decimal import Decimal
from domains.product import Product
from domains.product_repository_interface import IProductRepository
from infrastructures.database.models import ProductTable
from resources.dtos.product_get_dto import ProductGetDTO
from sqlalchemy import text

class ProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, product: Product) -> Product:
        """Save a new product and return it with the generated ID"""
        db_product = ProductTable(
            product_name=product.product_name,
            barcode=product.barcode,
            category=product.category,
            brand=product.brand,
            description=product.description,
            unit=product.unit,
            image_url=product.image_url,
            total_score=product.total_score
        )
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        
        return Product(
            id=db_product.id, 
            product_name=db_product.product_name,
            barcode=db_product.barcode or "", 
            category=db_product.category or "", 
            brand=db_product.brand or "", 
            description=db_product.description or "", 
            unit=db_product.unit or "", 
            image_url=db_product.image_url or "",
            total_score=db_product.total_score
        )
    
    def find_by_id(self, product_id: int) -> ProductGetDTO | None:
        """Find a product by ID"""
        statement = select(ProductTable).where(ProductTable.id == product_id)
        try:
            db_product = self.session.exec(statement).first()
        except Exception as e:
            return None
        if not db_product:
            return None
        return ProductGetDTO.model_validate(db_product)
    
    def find_by_barcode(self, barcode: str) -> Product | None:
        """Find a product by barcode"""
        statement = select(ProductTable).where(ProductTable.barcode == barcode)
        db_product = self.session.exec(statement).first()
        if not db_product:
                return None
        return Product(
                id=db_product.id, 
                product_name=db_product.product_name,
                barcode=db_product.barcode or "", 
                category=db_product.category or "", 
                brand=db_product.brand or "", 
                description=db_product.description or "", 
                unit=db_product.unit or "", 
                image_url=db_product.image_url or "",
                total_score=db_product.total_score
            )
    
    def find_by_name_like(self, search_text: str) -> list[Product]:
        limit = 50
        """Find products by advanced text matching with similarity ordering"""
        query = text("""
            WITH params AS (
            SELECT immutable_unaccent(lower(:search_text)) AS qstr
            )
            SELECT
                p.*,
                similarity(
                    immutable_unaccent(lower(p.product_name)),
                    params.qstr
                ) AS sim
            FROM products p, params
            WHERE immutable_unaccent(lower(p.product_name))
                ILIKE '%' || params.qstr || '%'
            ORDER BY
                sim DESC
            LIMIT :limit;
        """)

        query = query.bindparams(search_text=search_text, limit=limit)

        try:
            result = self.session.exec(query)
            db_products = result.all()
        except Exception as e:
            return []

        domain_products = []
        for db_product in db_products:
            current_product = Product(
                id=db_product.id, 
                product_name=db_product.product_name,
                barcode=db_product.barcode or "", 
                category=db_product.category or "", 
                brand=db_product.brand or "", 
                description=db_product.description or "", 
                unit=db_product.unit or "", 
                image_url=db_product.image_url or "",
                total_score=db_product.total_score
            )
            domain_products.append(current_product)
        return domain_products
    
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        statement = select(ProductTable).limit(limit)
        

        db_products = self.session.exec(statement).all()
        if not db_products:
            return []

        domain_products = []
        for p in db_products:
            current_product = Product(
                id=p.id, 
                product_name=p.product_name,  
                barcode=p.barcode or "", 
                category=p.category or "", 
                brand=p.brand or "", 
                description=p.description or "", 
                unit=p.unit or "", 
                image_url=p.image_url or "",
                total_score=p.total_score
            )
            domain_products.append(current_product)
        return domain_products