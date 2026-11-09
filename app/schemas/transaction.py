from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# Propriétés de base
class TransactionBase(BaseModel):
    date: date
    description: str = Field(..., min_length=2, max_length=255)
    montant: float = Field(..., gt=0, description="Le montant doit être supérieur à 0")
    categorie: Optional[str] = "Inconnu"

# Schéma pour la création (ce qu'on envoie)
class TransactionCreate(TransactionBase):
    pass

# Schéma pour la réponse (ce que l'API renvoie, avec l'ID)
class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True # Permet à Pydantic de lire depuis SQLAlchemy