from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import Path

from backend.graph import app as langgraph_app

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

# Serve frontend files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "frontend"),
    name="static"
)

@app.get("/", response_class=HTMLResponse)
def home():
    with open(BASE_DIR / "frontend" / "index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/ask")
def ask(question: str = Form(...)):
    try:
        state = {
            "question": question,
            "answer": "",
            "is_valid": False,
            "retries": 0
        }
        result = langgraph_app.invoke(state)
        # Return only JSON-serializable data
        return {
            "question": result.get("question", ""),
            "answer": result.get("answer", ""),
            "is_valid": result.get("is_valid", False),
            "retries": result.get("retries", 0)
        }
    except Exception as e:
        print(f"Error in /ask endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return {"error": str(e)}, 500

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)