from fastapi import FastAPI
from resources.product_resource import product_router
from contextlib import asynccontextmanager
from infrastructures.database.connection import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database and tables on startup"""
    create_db_and_tables()
    yield

app = FastAPI(
    docs_url="/",  # Swagger UI en la raíz
    redoc_url="/redoc",
    title="LiquiVerde Backend",
    description="API for LiquiVerde",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(product_router)