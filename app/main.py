from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base

# On importe le modèle pour que SQLAlchemy sache qu'il existe
from app.models import transaction 

# Création des tables dans la base de données au démarrage
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "message": "API de suivi de dépenses opérationnelle.",
        "documentation": "/docs"
    }