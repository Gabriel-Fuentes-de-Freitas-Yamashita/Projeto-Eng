from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database, auth, models

router = APIRouter(prefix="/insumos", tags=["insumos"])

print("ATRIBUTOS MODELS:", dir(models))

@router.post("/", response_model=schemas.Insumo)
def create_insumo(
    insumo: schemas.InsumoCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    restaurant = crud.get_restaurant(db, insumo.restaurant_id)
    if not restaurant or restaurant.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_insumo(db, insumo)

@router.get("/restaurant/{restaurant_id}", response_model=List[schemas.Insumo])
def read_insumos(
    restaurant_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    restaurant = crud.get_restaurant(db, restaurant_id)
    if not restaurant or restaurant.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_insumos_by_restaurant(db, restaurant_id)
