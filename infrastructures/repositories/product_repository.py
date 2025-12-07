from sqlmodel import Session, select
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
            image_url=product.image_url
        )
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        
        return Product(
            id=db_product.id, 
            product_name=db_product.product_name,
            barcode=db_product.barcode, 
            category=db_product.category,
            brand=db_product.brand, 
            description=db_product.description, 
            unit=db_product.unit, 
            image_url=db_product.image_url
        )
    
    def find_by_id(self, product_id: int) -> ProductGetDTO | None:
        """Find a product by ID"""
        statement = select(ProductTable).where(ProductTable.id == product_id)
        
        print(statement)
        try:
            db_product = self.session.exec(statement).first()
        except Exception as e:
            print(f"Error executing query: {e}")
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
                barcode=db_product.barcode, 
                category=db_product.category,
                brand=db_product.brand, 
                description=db_product.description, 
                unit=db_product.unit, 
                image_url=db_product.image_url,
                total_score=db_product.total_score if db_product.total_score else 0
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
            print(f"Error executing query: {e}")
            return []

        domain_products = []
        for db_product in db_products:
            current_product = Product(
                id=db_product.id, 
                product_name=db_product.product_name,
                barcode=db_product.barcode, 
                category=db_product.category,
                brand=db_product.brand, 
                description=db_product.description, 
                unit=db_product.unit, 
                image_url=db_product.image_url,
                total_score=db_product.total_score if db_product.total_score else 0
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
                barcode=p.barcode, 
                category=p.category,
                brand=p.brand, 
                description=p.description, 
                unit=p.unit, 
                image_url=p.image_url
            )
            domain_products.append(current_product)
        return domain_products