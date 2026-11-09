from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse

# On crée notre routeur avec un préfixe pour garder le code propre
router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"] # Ça créera une belle section dans Swagger
)

# 1. Route pour CRÉER une transaction
@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # On transforme le schéma Pydantic en modèle SQLAlchemy
    db_transaction = Transaction(**transaction.model_dump())
    
    # On sauvegarde en base
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction) # On rafraîchit pour récupérer l'ID généré
    
    return db_transaction

# 2. Route pour LISTER toutes les transactions
@router.get("/", response_model=List[TransactionResponse])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions