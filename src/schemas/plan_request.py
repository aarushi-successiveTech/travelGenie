from pydantic import BaseModel

class TravelRequest(BaseModel):
    budget: int
    destination: str
    days: int
    travel_type: str