
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers.users import router as users_router
from app.routers.expenses import router as expenses_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(users_router)
app.include_router(expenses_router)


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}
