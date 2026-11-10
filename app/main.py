from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.routers import transactions, analytics

from app.models import transaction 
from app.routers import transactions

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# On inclut les 2 routeurs avec notre préfixe d'API (/api/v1/transactions)
app.include_router(transactions.router, prefix=settings.API_V1_STR)
app.include_router(analytics.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "message": "API de suivi de dépenses opérationnelle.",
        "documentation": "/docs"
    }