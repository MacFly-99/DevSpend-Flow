from fastapi import FastAPI
from app.core.config import settings

# On initialise l'application FastAPI avec les infos de notre config
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# On crée notre première route (comme une route Symfony ou Next.js)
@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "message": "API de suivi de dépenses opérationnelle.",
        "documentation": "/docs"
    }