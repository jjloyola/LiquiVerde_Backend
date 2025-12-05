import os
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
from infrastructures.database.models import ProductTable

# Load environment variables
load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")  # Utilizar la variable de entorno correcta

if not DATABASE_URL:
    raise ValueError("USERS_DATABASE environment variable is not set")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True to see SQL queries in console

def create_db_and_tables():
    """Create database and tables"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Get database session (dependency for FastAPI)"""
    with Session(engine) as session:
        yield session