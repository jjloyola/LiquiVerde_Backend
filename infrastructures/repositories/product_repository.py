import datetime
from sqlmodel import Session, select
from decimal import Decimal
from domains.product import Product
from domains.product_repository_interface import IProductRepository
from infrastructures.database.models import ProductTable
from sqlalchemy import text

class ProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def _fill_product_from_db(self, db_product: ProductTable) -> Product:
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
            total_score=db_product.total_score or None,
            carbon_footprint=db_product.carbon_footprint or None,
            ecoscore_score=db_product.ecoscore_score or None,
            ecoscore_grade=db_product.ecoscore_grade or None,
            packaging_type=db_product.packaging_type or None,
            packaging_materials=db_product.packaging_materials or None,
            packaging_recyclable=db_product.packaging_recyclable or None,
            origin_country=db_product.origin_country or None,
            countries_tags=db_product.countries_tags or None,
            is_fair_trade=db_product.is_fair_trade or False,
            is_organic=db_product.is_organic or False,
            is_local=db_product.is_local or False,
            labels_tags=db_product.labels_tags or None,
            data_source=db_product.data_source or "open_food_facts",
            economic_score=db_product.economic_score or None,
            environmental_score=db_product.environmental_score or None,
            social_score=db_product.social_score or None,
        )

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
    
    def find_by_id(self, product_id: int) -> Product | None:
        """Find a product by ID"""
        statement = select(ProductTable).where(ProductTable.id == product_id)
        try:
            db_product = self.session.exec(statement).first()
        except Exception as e:
            return None
        if not db_product:
            return None
        return self._fill_product_from_db(db_product)
    
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
            current_product = self._fill_product_from_db(db_product)
            domain_products.append(current_product)
        
        return domain_products
    
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        statement = select(ProductTable).limit(limit)
        

        db_products = self.session.exec(statement).all()
        if not db_products:
            return []

        domain_products = []
        for db_product in db_products:
            current_product = self._fill_product_from_db(db_product)
            domain_products.append(current_product)
        return domain_products