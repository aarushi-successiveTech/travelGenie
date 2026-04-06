from src.features.pdf_generation.service import generate_pdf

def pdf_node(state): 
    data = state["input"]
    processing = state["processing_output"]
    budget = state["budget_output"]
    itinerary = state["itinerary_output"]

    file_path = generate_pdf(data, processing, budget, itinerary)

    state["pdf_path"] = file_path
    return state
