from domains.product import Product
from domains.product_repository_interface import IProductRepository

class ProductRepository(IProductRepository):
    def __init__(self):
        self.products: list[Product] = [Product(id=1, name="Product 1", price=100), Product(id=2, name="Product 2", price=200), Product(id=3, name="Product 3", price=300)] #database simulation

    def save(self, product: Product) -> Product:
        """Save a new product and return it with the generated ID"""
        self.products.append(product)
        return product
    
    def find_by_id(self, product_id: int) -> Product | None:
        """Find a product by ID"""
        return next((product for product in self.products if product.id == product_id), None)
    
    def find_all(self, limit: int) -> list[Product]:
        """Get all products"""
        return self.products[:limit]