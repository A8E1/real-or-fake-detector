from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="Real or Fake API (stub)")

class PredictResponse(BaseModel):
    score: float
    label: str
    model_version: str
    
    
@app.get("/health")
def health():
    return {"status": "ok", "model_version": "stub-v0"}

@app.post("/predict", response_model=PredictResponse)
async def predict(file: UploadFile = File(...)):
    _ = await file.read()
    score = 0.42 # fixed dummy score
    label = "fake" if score >= 0.5 else "real"
    return {"score": score, "label": label, "model_version": "stub-v0"}