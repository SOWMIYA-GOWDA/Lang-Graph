from typing import TypedDict

class GraphState(TypedDict):
    question: str
    answer: str
    is_valid: bool
    retries: int