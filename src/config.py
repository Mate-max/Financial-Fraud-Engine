from pathlib import Path

# პროექტის ძირითადი დეტექტორია (Financial-Fraud-Engine)
BASE_DIR = Path(__file__).resolve().parent.parent

# ფაილების მისამართები
DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "creditcard.csv"

# ML მოდელის პარამეტრები
TARGET_COLUMN = "Class"
RANDOM_STATE = 42
TEST_SIZE = 0.2