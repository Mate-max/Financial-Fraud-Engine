import pandas as pd
from pathlib import Path
from src.config import RAW_DATA_PATH

def load_raw_data(data_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """"
    ტვირთავს თავდაპირველ CSV მონაცემებს Pandas DataFrame-ში
    """

    if not data_path.exists():
        raise FileNotFoundError(f"მონაცემთა ფაილი ვერ მოიძებნა მისამართზე: {data_path}")

    print(f"მონაცემების ჩატვირთვა ფაილიდან: {data_path.name}...")
    df = pd.read_csv(data_path)
    print(f"წარმატებით ჩაიტვირთა {df.shape[0]} სტრიქონი და {df.shape[1]} სვეტი.")

    return df

if __name__ == "__main__":
    # ფაილის პირდაპირ გაშვებისას შევამოწმოთ ფუნქციის მუშაობა
    data = load_raw_data()
    print("\nპირველი 5 ჩანაწერი:")
    print(data.head())