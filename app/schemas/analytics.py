from pydantic import BaseModel
from typing import List

class CategoryTotal(BaseModel):
    categorie: str
    total: float

class AnalyticsSummary(BaseModel):
    total_general: float
    total_par_categorie: List[CategoryTotal]