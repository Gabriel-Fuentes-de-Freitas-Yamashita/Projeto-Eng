from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, insumos, reports

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas
app.include_router(users.router)
app.include_router(insumos.router)
app.include_router(reports.router)
