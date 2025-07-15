from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Input(BaseModel):
    text: str

@app.post("/explain")
def explain(input: Input):
    prompt = f"Explain this scientific text simply and accurately:\n\n{input.text}"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    output = response.json()["response"]
    return {"explanation": output}
