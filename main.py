from fastapi import FastAPI
from resources.product_resource import product_router

app = FastAPI(
    docs_url="/",  # Swagger UI en la raíz
    redoc_url="/redoc",
    title="LiquiVerde Backend",
    description="API for LiquiVerde",
    version="1.0.0",
)


app.include_router(product_router)