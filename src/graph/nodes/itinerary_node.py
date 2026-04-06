from src.features.itinerary_generation.service import generate_itinerary
from src.features.budget_allocation.budget_interpreter import interpret_budget

def itinerary_node(state): 

    data = state["input"]
    processing = state["processing_output"]
    budget = state["budget_output"]

    budget_context = interpret_budget(budget, data["days"])
    result = generate_itinerary(data, processing, budget_context)

    state["itinerary_output"] = result
    return state 