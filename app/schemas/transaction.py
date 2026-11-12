from pydantic import BaseModel, Field, ConfigDict # <-- 1. Ajoute ConfigDict ici
from datetime import date
from typing import Optional

class TransactionBase(BaseModel):
    date: date
    description: str = Field(..., min_length=2, max_length=255)
    montant: float = Field(..., gt=0, description="Le montant doit être supérieur à 0")
    categorie: Optional[str] = "Inconnu"

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    
    # 2. Remplace le "class Config" par cette ligne :
    model_config = ConfigDict(from_attributes=True)