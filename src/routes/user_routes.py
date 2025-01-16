from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Carte, Cititor, Imprumut
from src.schemas.user_schemas import CarteBase, CarteCreate, Carte as UserSchema
from typing import List

router = APIRouter(prefix="/users", tags=["users"])



@router.get("/carti/", response_model=list[UserSchema])
#@router.get("/", response_model=list[UserSchema])
def get_carti(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Carte).offset(skip).limit(limit).all()


@router.post("/carti/", response_model=UserSchema)
#@router.post("/", response_model=UserSchema)
def create_carte(carte: CarteCreate, db: Session = Depends(get_db)):
    db_carte = db.query(Carte).filter(Carte.isbn == carte.isbn).first()
    if db_carte:
        raise HTTPException(status_code=400, detail="Carte deja înregistrată")

    db_carte = Carte(
        titlu=carte.titlu,
        autor=carte.autor,
        isbn=carte.isbn
    )
    db.add(db_carte)
    db.commit()
    db.refresh(db_carte)
    return db_carte



@router.put("/carti/{carte_id}", response_model=UserSchema)
#@router.put("/{carte_id}", response_model=UserSchema)
def update_carte(carte_id: int, carte: CarteCreate, db: Session = Depends(get_db)):
    #db_carte = update_carte(db=db, carte_id=carte_id, carte=carte)
    db_carte = db.query(Carte).filter(Carte.id == carte_id).first()
    if db_carte is None:
        raise HTTPException(status_code=404, detail="Carte nu a fost găsită")

    db_carte.titlu = carte.titlu
    db_carte.autor = carte.autor
    db_carte.isbn = carte.isbn
    db.commit()
    db.refresh(db_carte)
    return db_carte

@router.delete("/carti/{carte_id}", response_model=UserSchema)
#@router.delete("/{carte_id}", response_model=UserSchema)
def delete_carte(carte_id: int, db: Session = Depends(get_db)):
    #db_carte = delete_carte(db=db, carte_id=carte_id)
    db_carte = db.query(Carte).filter(Carte.id == carte_id).first()
    if db_carte is None:
        raise HTTPException(status_code=404, detail="Carte nu a fost găsită")

    db.delete(db_carte)
    db.commit()
    return db_carte