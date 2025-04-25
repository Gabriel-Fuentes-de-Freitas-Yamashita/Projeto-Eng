from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database, auth, models

router = APIRouter(prefix="/reports", tags=["reports"])

@router.post("/", response_model=schemas.Report)
def create_report(
    report: schemas.ReportCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    restaurant = crud.get_restaurant(db, report.restaurant_id)
    if not restaurant or restaurant.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_report(db, report)

@router.get("/restaurant/{restaurant_id}", response_model=List[schemas.Report])
def read_reports(
    restaurant_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    restaurant = crud.get_restaurant(db, restaurant_id)
    if not restaurant or restaurant.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_reports_by_restaurant(db, restaurant_id)
