# MLOps Pipeline Project - Machine Learning in Production

🌐 This project is also available in: 🇧🇷 [Português](readme.pt.md)

[![CI](https://github.com/fogata/mlops-project/actions/workflows/ci.yml/badge.svg)](https://github.com/fogata/mlops-project/actions/workflows/ci.yml)

## 📌 Project Overview

This project demonstrates a modern and professional MLOps pipeline using cloud-native tools for model versioning, deployment, and monitoring.

It aims to help software engineers and data scientists implement a reproducible, automated, and production-ready ML lifecycle.

## 🛠️ Technologies Used

- **Python 3.10+**
- **FastAPI** – for serving ML models as RESTful APIs
- **scikit-learn** – model training and validation
- **DVC** – data and model versioning
- **Docker** – containerization
- **Render** – cloud deployment platform
- **GitHub Actions** – CI for testing and validation
- **MLflow (planned)** – experiment tracking
- **Evidently (planned)** – model monitoring and drift detection

## 🚀 Features

- [x] REST API with FastAPI (`/predict`)
- [x] Model training with DVC and scikit-learn
- [x] Automated training at deployment if model is missing
- [x] CI/CD with GitHub Actions
- [x] Deployment on Render.com with `render.yaml`

## 🧪 API Access via Render

Application is deployed on Render. Use the following endpoints:

- Swagger Docs:  
  👉 `https://mlops-api.onrender.com/docs`

- Inference endpoint:  
  `POST https://mlops-api.onrender.com/predict`

### Example Request:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Expected response:

```json
{
  "prediction": [0]
}
```

> The model is trained automatically on first deployment if not already present.

## 📁 Project Structure

```text
mlops-project/
├── .github/             # CI workflows
├── data/                # Versioned data (DVC)
├── notebooks/           # Exploratory notebooks
├── src/
│   ├── training/        # Model training scripts
│   ├── serving/         # FastAPI endpoints and model loading
│   └── utils/           # Helper utilities
├── models/              # Trained model (.pkl)
├── render.yaml          # Render deploy config
├── Dockerfile
├── requirements.txt
├── dvc.yaml
├── .gitignore
└── README.md
```

## 📝 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

[![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

## ✉️ Contact

Felipe Ogata  
📧 [felipeogata@gmail.com](mailto:felipeogata@gmail.com)
