from fastapi import FastAPI
from pydantic import BaseModel
from serving.model_loader import load_model
import numpy as np

app = FastAPI(
    title="MLOps API",
    description="API para inferência de modelo treinado com DVC",
    version="1.0"
)

# Carrega o modelo ao iniciar
model = load_model()

# Modelo de entrada esperado
class InputData(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "API de inferência está no ar! Acesse /docs para testar."}

@app.post("/predict")
def predict(data: InputData):
    features_array = np.array([data.features])
    prediction = model.predict(features_array)
    return {"prediction": prediction.tolist()}
