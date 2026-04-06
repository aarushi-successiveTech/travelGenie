from fastapi import APIRouter
from src.schemas.plan_request import TravelRequest
from src.graph.builder import build_graph
from fastapi.responses import FileResponse
import uuid
from src.core.trip_store import trip_store

router = APIRouter()
graph = build_graph()

@router.post("/plan")
def process_plan(request: TravelRequest):

    data = request.dict()
    result = graph.invoke({
        "input": data, 
        "processing_output": {},
        "budget_output": {},
        "itinerary_output": {},
    })

    trip_id = str(uuid.uuid4())
    trip_store[trip_id] = result

    return{
        "message": "Plan received successfully", 
        "trip_id": trip_id,
        "data": request, 
        "ai_output": result.get("processing_output"), 
        # "budget_output": result.get("budget_output"),
        "itinerary_output": result.get("itinerary_output"),
        # "pdf_path": result.get("pdf_path")
    }

@router.post("/budget_split")
def get_budget_split(trip_id: str): 

    budget_split = trip_store.get(trip_id)
    if not budget_split: 
        return {"error": "Invalid Trip Id"}
    return {
        "message": "Day-wise budget generated successfully", 
        "budget_split": budget_split.get("budget_output")
    }

@router.post("/generate_pdf")
def get_pdf(trip_id: str): 

    pdf_output = trip_store.get(trip_id)
    if not pdf_output: 
        return {"error": "Invalid trip Id"}
    
    return FileResponse(
        path=pdf_output.get("pdf_path"),
        filename="trip_plan.pdf", 
        media_type="application/pdf"
    )