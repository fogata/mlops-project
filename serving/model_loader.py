import joblib
import os
from training.train import main as train_model_if_needed

MODEL_PATH = os.path.join("models", "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        print("Modelo não encontrado. Executando treinamento automático...")
        train_model_if_needed()
    return joblib.load(MODEL_PATH)
