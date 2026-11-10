from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.transaction import Transaction
from app.schemas.analytics import AnalyticsSummary, CategoryTotal

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/summary", response_model=AnalyticsSummary)
def get_analytics_summary(db: Session = Depends(get_db)):
    # 1. Calcul du total général
    total_general = db.query(func.sum(Transaction.montant)).scalar() or 0.0
    
    # 2. Calcul du total par catégorie (le GROUP BY de SQL)
    results = db.query(
        Transaction.categorie, 
        func.sum(Transaction.montant).label("total")
    ).group_by(Transaction.categorie).all()
    
    # 3. On formate les résultats
    total_par_categorie = [
        CategoryTotal(categorie=row.categorie, total=row.total) 
        for row in results
    ]
    
    # On trie par montant décroissant
    total_par_categorie.sort(key=lambda x: x.total, reverse=True)
    
    return AnalyticsSummary(
        total_general=total_general,
        total_par_categorie=total_par_categorie
    )