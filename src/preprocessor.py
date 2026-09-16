import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from src.config import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE

def preprocessor_data(df: pd.DataFrame):
    """
    ამუშავებს მონაცემებს:
    1. ახდენს Amount და Time სვეტების სტანდარტიზაციას (Scaling)
    2. ყოფს მონაცემებს Train და Test სიმრავლეებად
    3. იყენებს SMOTE-ს Class Imbalance-ის გადასაჭრელად (მხოლოდ Train-ზე)
    """
    df_clean = df.copy()

    # 1. Scaling: Amount & Time სვეტების გათანაბრება
    scaler = StandardScaler()
    df_clean['scaled_amount'] = scaler.fit_transform(df_clean[['Amount']])
    df_clean['scaled_time'] = scaler.fit_transform(df_clean[['Time']])

    # ვშლით ორიგინალ unscaled სვეტებს
    df_clean.drop(['Time', 'Amount'], axis=1, inplace=True)

    # 2. X (Features) & Y (Target) გამოყოფა
    X = df_clean.drop(TARGET_COLUMN, axis=1)
    y = df_clean[TARGET_COLUMN]

    # 3. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    # 4. SMOTE (Oversampling) - იქმნება სინთეზური თაღლითური მონაცემები მხოლოდ Train-ისთვის
    print("SMOTE-ის გამოყენება Class Imbalance-ის გასასწორებლად...")
    smote = SMOTE(random_state=RANDOM_STATE)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    print(f"საწყისი Train ზომა: {y_train.value_counts().to_dict()}")
    print(f"SMOTE-ის შემდეგ Train ზომა: {y_train_resampled.value_counts().to_dict()}")

    return X_train_resampled, X_test, y_train_resampled, y_test

if __name__ == "__main__":
    from src.data_loader import load_raw_data

    raw_df = load_raw_data()
    X_train, X_test, y_train, y_test = preprocessor_data(raw_df)
    print("\nმონაცემების დამუშავება წარმატებით დასრულდა!")