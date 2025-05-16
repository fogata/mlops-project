import joblib
import os

MODEL_PATH = os.path.join("models", "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}. Rode o script de treinamento primeiro.")
    return joblib.load(MODEL_PATH)
