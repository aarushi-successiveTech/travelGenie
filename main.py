from fastapi import FastAPI
from src.routes.plan_route import router as plan_router

app = FastAPI()

@app.get("/")
def home(): 
    return{"message": "TripGenie backend running"}

app.include_router(plan_router)