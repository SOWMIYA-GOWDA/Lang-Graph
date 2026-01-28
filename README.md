
# LangGraph with Validation and Retry Logic

A simple yet structured application built using FastAPI, LangGraph, and Gemini LLM.
This project demonstrates how to combine AI generation with validation logic and controlled workflows for reliable outputs.

# 🚀 Features

- User-friendly interface for interaction
- AI-powered responses using an LLM
- Structured workflow using LangGraph
- Rule-based validation logic
- Retry handling for improved results
- Clear frontend–backend separation

# 🧠 Tech Stack

**Backend:** FastAPI (Python)

**Workflow Engine:** LangGraph

**LLM:** Gemini

**Frontend:** HTML, CSS, JavaScript

**Environment:** Python Virtual Environment

# 📂 Project Structure

```text

Langraph/
├── app.py
├── backend/
│ ├── init.py
│ ├── graph.py
│ ├── nodes.py
│ └── schema.py
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── .env
├── requirements.txt

# ⚙️ How It Works

- User submits input from the frontend
- FastAPI handles the request
- LangGraph initializes workflow state
- LLM generates a response
- Output is validated using rules
- If invalid, the workflow retries once
- Final result is returned to the UI

# 🧪 Validation Logic

- Output must not be empty
- Minimum content length enforced
- Maximum retry limit applied
