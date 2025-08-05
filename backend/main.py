from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["chrome-extension://<your-extension-id>"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Input(BaseModel):
    text: str

@app.post("/explain")
def explain(input: Input):
    prompt = f"Explain this scientific text simply and accurately:\n\n{input.text}"
    
    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama",  # or another smaller model
        "prompt": prompt,
        "stream": False
    }
)
    try:
        data = response.json()
    except Exception:
        return {"error": "Failed to parse Ollama response", "raw": response.text}
    if "response" not in data:
        # Log the full Ollama response for debugging
        print("Ollama error:", data)
        return {"error": "Ollama error", "details": data}
    return {"explanation": data["response"]}

app.options("/explain")
def options_explain():
    return Response(status_code=200)