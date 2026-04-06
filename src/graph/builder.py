from langgraph.graph import StateGraph
from src.graph.state import TravelState
from src.graph.nodes.processing_node import data_processing_node
from src.graph.nodes.budget_node import budget_node
from src.graph.nodes.itinerary_node import itinerary_node
from src.graph.nodes.pdf_node import pdf_node

def build_graph(): 
    graph = StateGraph(TravelState)

    graph.add_node("ai_processing_node", data_processing_node)
    graph.add_node("budget_node", budget_node)
    graph.add_node("itinerary_node", itinerary_node)
    graph.add_node("pdf_node", pdf_node)

    graph.set_entry_point("ai_processing_node")
    graph.add_edge("ai_processing_node", "budget_node")
    graph.add_edge("budget_node", "itinerary_node")
    graph.add_edge("itinerary_node", "pdf_node")
    graph.set_finish_point("pdf_node")

    return graph.compile()