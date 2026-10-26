
from fastapi import FastAPI

app = FastAPI(title="Expense Tracker API")


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}
