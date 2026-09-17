from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from typing import List
from src.model import MODEL_PATH

app = FastAPI(
    title="Financial Fraud Detection API",
    description="ML-powered API for real-time transaction fraud detection",
    version="1.0.0"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"მოდელის ჩატვირთვა ვერ მოხერხდა: {e}")

# XGBoost-ის სვეტების ზუსტი თანმიმდევრობა preprocessor.py-ს მიხედვით
FEATURE_NAMES = [f'V{i}' for i in range(1, 29)] + ['scaled_amount', 'scaled_time']

class TransactionData(BaseModel):

    # features: List[float] = Field(
    #     ..., 
    #     description="30 ნიშანი: [V1, V2, ..., V28, scaled_amount, scaled_time]",
    #     example=[0.0] * 28 + [0.1, -0.5]
    # )
    features: List[float] = Field(..., json_schema_extra={"example": [0.0] * 30})

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}

@app.post("/predict")
def predict_fraud(transaction: TransactionData):
    if len(transaction.features) != 30:
        raise HTTPException(
            status_code=400, 
            detail=f"მონაცემები უნდა შეიცავდეს ზუსტად 30 ნიშანს. მიღებულია: {len(transaction.features)}"
        )
    
    # მონაცემების გადაყვანა DataFrame-ში სვეტების სწორი თანმიმდევრობით
    input_data = pd.DataFrame([transaction.features], columns=FEATURE_NAMES)
    
    prediction = int(model.predict(input_data)[0])
    probability = float(model.predict_proba(input_data)[0][1])
    
    return {
        "is_fraud": bool(prediction),
        "fraud_probability": round(probability, 4),
        "risk_level": "HIGH" if probability > 0.7 else ("MEDIUM" if probability > 0.3 else "LOW")
    }