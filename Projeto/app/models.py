from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


print(">>> MODELS.PY CARREGADO COM SUCESSO <<<")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    restaurants = relationship("Restaurant", back_populates="owner")

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="restaurants")
    insumos = relationship("Insumo", back_populates="restaurant")
    reports = relationship("Report", back_populates="restaurant")

class Insumo(Base):
    __tablename__ = "insumos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="insumos")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    type = Column(String, nullable=False)
    created_at = Column(DateTime)
    restaurant = relationship("Restaurant", back_populates="reports")
