from langgraph.graph import StateGraph, END
from backend.schema import GraphState
from backend.nodes import answer_generator, answer_validator

def route_logic(state: GraphState):
    if state["is_valid"]:
        return "end"
    if state["retries"] < 1:
        return "generate"
    return "end"

graph = StateGraph(GraphState)

graph.add_node("generate", answer_generator)
graph.add_node("validate", answer_validator)

graph.set_entry_point("generate")
graph.add_edge("generate", "validate")

graph.add_conditional_edges(
    "validate",
    route_logic,
    {
        "generate": "generate",
        "end": END
    }
)

app = graph.compile()