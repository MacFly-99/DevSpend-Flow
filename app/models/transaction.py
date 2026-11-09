from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    montant = Column(Float, nullable=False)
    categorie = Column(String, default="Inconnu")