from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()

def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_rest = models.Restaurant(**restaurant.dict())
    db.add(db_rest)
    db.commit()
    db.refresh(db_rest)
    return db_rest

def get_insumos_by_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Insumo).filter(models.Insumo.restaurant_id == restaurant_id).all()

def create_insumo(db: Session, insumo: schemas.InsumoCreate):
    db_ins = models.Insumo(**insumo.dict())
    db.add(db_ins)
    db.commit()
    db.refresh(db_ins)
    return db_ins

def get_reports_by_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Report).filter(models.Report.restaurant_id == restaurant_id).all()

def create_report(db: Session, report: schemas.ReportCreate):
    db_rep = models.Report(**report.dict(), created_at=datetime.utcnow())
    db.add(db_rep)
    db.commit()
    db.refresh(db_rep)
    return db_rep
