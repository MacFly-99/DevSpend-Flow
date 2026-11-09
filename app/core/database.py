from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# 1. Création du moteur (engine) SQLite
# check_same_thread=False est requis uniquement pour SQLite avec FastAPI
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 2. Création d'une usine à sessions (pour faire des requêtes à la BDD)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. La classe de base pour nos futurs modèles (tables)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()