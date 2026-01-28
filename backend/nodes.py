import os
import google.generativeai as genai
from backend.schema import GraphState

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def answer_generator(state: GraphState) -> GraphState:
    try:
        print(f"Generating answer for question: {state['question']}")
        response = model.generate_content(state["question"])
        print(f"Response: {response}")
        print(f"Response text: {response.text if hasattr(response, 'text') else 'No text attribute'}")
        answer = response.text or ""
        print(f"Final answer: {answer}")

        return {
            **state,
            "answer": answer,
            "retries": state["retries"] + 1
        }
    except Exception as e:
        print(f"Error in answer_generator: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            **state,
            "answer": f"Error: {str(e)}",
            "retries": state["retries"] + 1
        }

def answer_validator(state: GraphState) -> GraphState:
    answer = state["answer"]
    is_valid = bool(answer) and len(answer) >= 50

    return {
        **state,
        "is_valid": is_valid
    }