import xgboost as xgb
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import joblib
from pathlib import Path

from src.config import BASE_DIR, RANDOM_STATE
from src.data_loader import load_raw_data
from src.preprocessor import preprocessor_data

# მოდელის შესანახი საქაღალდე
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "xgboost_fraud_model.pkl"

def train_and_evaluate():
    # 1. ჩავტვირთოთ და დავამუშაოთ მონაცემები
    raw_df = load_raw_data()
    X_train, X_test, y_train, y_test = preprocessor_data(raw_df)

    # 2. XGBoost მოდელის ინიციალიზაცია და სწავლება
    print("\n[INFO] XGBoost მოდელის სწავლება მიმდინარეობს...")
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    print("[SUCCESS] მოდელის სწავლება დასრულდა!")

    # 3. შეფასება საგამოცდო (Test) მონაცემებზე
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("\n--- მოდელის შეფასების რეპორტი ---")
    print(classification_report(y_test, y_pred))

    roc_auc = roc_auc_score(y_test, y_proba)
    print(f"ROC-AUC Score: {roc_auc:.4f}")

    print("\nConfusion Matrix (შეცდომების მატრიცა):")
    print(confusion_matrix(y_test, y_pred))

    # 4. მოდელის შენახვა დისკზე
    joblib.dump(model, MODEL_PATH)
    print(f"\n[INFO] მოდელი წარმატებით შენახულია: {MODEL_PATH}")

if __name__ == "__main__":
    train_and_evaluate()