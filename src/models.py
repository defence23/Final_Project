from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Carte(Base):
    __tablename__ = "carti"
    id = Column(Integer, primary_key=True, index=True)
    titlu = Column(String, index=True)
    autor = Column(String)
    isbn = Column(String, unique=True)

    imprumuturi = relationship("Imprumut", back_populates="carte")

class Cititor(Base):
    __tablename__ = "cititori"
    id = Column(Integer, primary_key=True, index=True)
    nume = Column(String, index=True)
    email = Column(String, unique=True)

    imprumuturi = relationship("Imprumut", back_populates="cititor")

class Imprumut(Base):
    __tablename__ = "imprumuturi"
    id = Column(Integer, primary_key=True, index=True)
    carte_id = Column(Integer, ForeignKey("carti.id"))
    cititor_id = Column(Integer, ForeignKey("cititori.id"))

    carte = relationship("Carte", back_populates="imprumuturi")
    cititor = relationship("Cititor", back_populates="imprumuturi")