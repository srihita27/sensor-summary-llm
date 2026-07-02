import pandas as pd

from src.feature_engineering import FeatureEngineer
from src.anamoly_detection import AnomalyDetector


print("=" * 60)

print("Loading cleaned dataset...")

df = pd.read_csv("data/processed/cleaned_sensor.csv")

engineer = FeatureEngineer(window_size=100)

windows = engineer.split_windows(df)

detector = AnomalyDetector()

feature_rows = []

for window in windows:

    features = engineer.extract_features(window)

    anomalies = detector.detect(window)

    features.update(anomalies)

    feature_rows.append(features)

final_df = pd.DataFrame(feature_rows)

final_df.to_csv(
    "data/processed/window_features_with_anomalies.csv",
    index=False
)

print(final_df.head())

print()

print("Total Windows:", len(final_df))

print()

print("Saved Successfully!")

print("=" * 60)