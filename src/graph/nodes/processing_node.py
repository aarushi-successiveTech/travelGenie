from src.features.planning.service import planning_input

def data_processing_node(state):
    data = state["input"]

    result = planning_input(data)
    state["processing_output"] = result
    return state
