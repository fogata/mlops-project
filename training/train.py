# src/training/train.py

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Caminho onde o modelo será salvo
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

def load_data():
    """Carrega o dataset Iris e divide em treino e teste."""
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name="target")
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    """Treina um modelo RandomForest."""
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo e imprime a acurácia."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {acc:.4f}")

def save_model(model):
    """Salva o modelo treinado como arquivo .pkl."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Modelo salvo em: {MODEL_PATH}")

def main():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)

if __name__ == "__main__":
    main()
