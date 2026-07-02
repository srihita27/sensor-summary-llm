import pandas as pd

from src.feature_engineering import FeatureEngineer

print("=" * 60)

print("Loading cleaned dataset...")

df = pd.read_csv("data/processed/cleaned_sensor.csv")

engineer = FeatureEngineer(window_size=100)

feature_df = engineer.generate_feature_dataframe(df)

feature_df.to_csv(
    "data/processed/window_features.csv",
    index=False
)

print(feature_df.head())

print()

print("Number of windows:", len(feature_df))

print()

print("Saved feature dataset.")

print("=" * 60)