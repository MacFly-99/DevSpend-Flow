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

# 3. Route pour RÉCUPÉRER une transaction par son ID
@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    
    # GESTION DE L'ERREUR : Si la transaction n'existe pas (None)
    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"La transaction avec l'ID {transaction_id} n'existe pas."
        )
        
    return transaction