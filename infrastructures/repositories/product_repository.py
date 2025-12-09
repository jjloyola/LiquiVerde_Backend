import datetime
from sqlmodel import Session, select
from decimal import Decimal
from domains.product import ProductWithStore
from domains.product_repository_interface import IProductRepository
from domains.product_store_with_price import ProductStoreWithPrice
from infrastructures.database.models import ProductTable
from sqlalchemy import text

class ProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def _fill_one_product_from_db(self, db_product: ProductTable) -> ProductWithStore:
        if not db_product:
            return None
        return ProductWithStore(
            id=db_product.id,
            product_name=db_product.product_name,
            barcode=db_product.barcode,
            category=db_product.category,
            brand=db_product.brand,
            description=db_product.description,
            unit=db_product.unit,
            image_url=db_product.image_url,
            total_score=db_product.total_score,
            carbon_footprint=db_product.carbon_footprint,
            ecoscore_score=db_product.ecoscore_score,
            ecoscore_grade=db_product.ecoscore_grade,
            packaging_type=db_product.packaging_type,
            packaging_materials=db_product.packaging_materials,
            packaging_recyclable=db_product.packaging_recyclable,
            origin_country=db_product.origin_country,
            countries_tags=db_product.countries_tags,
            is_fair_trade=db_product.is_fair_trade,
            is_organic=db_product.is_organic,
            is_local=db_product.is_local,
            labels_tags=db_product.labels_tags,
            data_source=db_product.data_source,
            economic_score=db_product.economic_score,
            environmental_score=db_product.environmental_score,
            social_score=db_product.social_score,
            
        )
    def fill_product_with_stores(self, db_product: ProductTable) -> ProductWithStore:
       
        
        
        product_store_with_price_list: list[ProductStoreWithPrice] = []
        for i  in range(len(db_product.product_stores)):
            product_store = db_product.product_stores[i]
            store = db_product.stores[i]
            product_store_with_price = ProductStoreWithPrice(
                    store_id=store.id,
                    product_id=db_product.id,
                    store_name=store.name,
                    price=product_store.price,
                    availability=product_store.availability,
                    stock_quantity=product_store.stock_quantity,
                ) 
            product_store_with_price_list.append(product_store_with_price)
        
        
        product_with_store = ProductWithStore(
            id=db_product.id,
            product_name=db_product.product_name,
            barcode=db_product.barcode,
            category=db_product.category,
            brand=db_product.brand,
            description=db_product.description,
            unit=db_product.unit,
            image_url=db_product.image_url,
            total_score=db_product.total_score,
            carbon_footprint=db_product.carbon_footprint,
            ecoscore_score=db_product.ecoscore_score,
            ecoscore_grade=db_product.ecoscore_grade,
            packaging_type=db_product.packaging_type,
            packaging_materials=db_product.packaging_materials,
            packaging_recyclable=db_product.packaging_recyclable,
            origin_country=db_product.origin_country,
            countries_tags=db_product.countries_tags,
            is_fair_trade=db_product.is_fair_trade,
            is_organic=db_product.is_organic,
            is_local=db_product.is_local,
            labels_tags=db_product.labels_tags,
            data_source=db_product.data_source,
            economic_score=db_product.economic_score,
            environmental_score=db_product.environmental_score,
            social_score=db_product.social_score,
            product_stores_with_price=product_store_with_price_list
        )

      
        return product_with_store

    def save(self, product: ProductWithStore) -> ProductWithStore:
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
        
        return self._fill_one_product_from_db(db_product)
    
    def find_by_id(self, product_id: int) -> ProductWithStore | None:
        """Find a product by ID"""
        statement = select(ProductTable).where(ProductTable.id == product_id)
        try:
            db_product = self.session.exec(statement).first()
        except Exception as e:
            return None
        if not db_product:
            return None
        return self._fill_one_product_from_db(db_product)
    
    def find_by_barcode(self, barcode: str) -> ProductWithStore | None:
        """Find a product by barcode"""
        statement = select(ProductTable).where(ProductTable.barcode == barcode)
        db_product: ProductTable = self.session.exec(statement).first()
        if not db_product:
                return None
        return self.fill_product_with_stores(db_product)
    
    def find_by_name_like(self, search_text: str) -> list[ProductWithStore]:
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
            current_product = self._fill_one_product_from_db(db_product)
            domain_products.append(current_product)
        
        return domain_products
    
    def find_all(self, limit: int) -> list[ProductWithStore]:
        """Get all products"""
        statement = select(ProductTable).limit(limit)
        

        db_products = self.session.exec(statement).all()
        if not db_products:
            return []

        domain_products = []
        for db_product in db_products:
            current_product = self._fill_one_product_from_db(db_product)
            domain_products.append(current_product)
        return domain_products