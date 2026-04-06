from typing import TypedDict, Dict, Any

class TravelState(TypedDict): 
    input: Dict[str, Any]
    processing_output: Dict[str, Any]
    budget_output: Dict[str, Any]
    itinerary_output: Dict[str, Any]
    booking_output: Dict[str, Any]
    pdf_path: str

# budget output - separate 
# generate pdf 
# user validation layer 