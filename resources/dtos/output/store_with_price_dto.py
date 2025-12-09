from decimal import Decimal


class ProductStoreWithPriceDto:
    store_id:int
    product_id:int
    
    store_name:str
    price:Decimal
    availability:bool
    stock_quantity:int