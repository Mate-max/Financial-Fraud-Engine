#  ლაივ საიტის ლინკი
https://financial-fraud-engine.onrender.com/docs

# 🛡️ Financial Fraud Detection Engine

An end-to-end, production-ready Machine Learning API for detecting financial transaction fraud in real-time. Built with **XGBoost**, **FastAPI**, containerized via **Docker**, and deployed with fully automated **CI/CD via GitHub Actions**.

---

## 🚀 Live Demo & API Documentation

- **Live Service**: https://financial-fraud-engine.onrender.com/docs

---

## 🛠️ Tech Stack & Tools

- **Machine Learning**: XGBoost, Scikit-Learn, Imbalanced-Learn (SMOTE)
- **API Framework**: FastAPI, Pydantic V2, Uvicorn
- **Containerization & Deployment**: Docker, Render
- **Testing & Quality Assurance**: Pytest, HTTPX
- **CI/CD Pipeline**: GitHub Actions
- **Environment**: WSL 2 / Python 3.10

---

## 📌 Features

* **High-Precision Inference**: Uses XGBoost trained on highly imbalanced credit card fraud transaction datasets.
* **Preprocessed Pipelines**: Integrated `SMOTE` and standard scalers for input transformation.
* **Automated CI/CD**: Every push to `main` runs unit & integration tests via GitHub Actions.
* **Production-Grade API**: Includes data validation via Pydantic and async request handling.

---

## 💻 Local Setup & Execution

### 1. Clone & Set Up Environment
```bash
git clone [https://github.com/Mate-max/Financial-Fraud-Engine.git](https://github.com/Mate-max/Financial-Fraud-Engine.git)
cd Financial-Fraud-Engine
python -m venv venv
source venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
## Run API Locally
uvicorn app.main:app --reload

Visit http://127.0.0.1:8000/docs to test endpoints via Swagger UI.

## Run Tests
python -m pytest

## Docker Deployment
To build and run the Docker container locally:
docker build -t fraud-detection-api .
docker run -p 8000:8000 fraud-detection-api
