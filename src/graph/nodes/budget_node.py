from src.features.budget_allocation.service import allocate_budget

def budget_node(state): 
    data = state["input"]
    processing = state["processing_output"]

    result = allocate_budget(data, processing)
    state["budget_output"] = result

    return state 