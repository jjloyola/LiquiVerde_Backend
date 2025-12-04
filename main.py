from fastapi import FastAPI
from resources.product_resource import product_router

app = FastAPI(
    docs_url="/",  # Swagger UI en la raíz
    redoc_url="/redoc",
    title="Mi API",
    description="API con Arquitectura Limpia",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(product_router)