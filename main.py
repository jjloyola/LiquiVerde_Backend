from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Origen que quieres permitir
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"]  # Encabezados permitidos
)


app.include_router(product_router)