import pandas as pd

from src.summarizer import summarize

print("=" * 60)

df = pd.read_csv(
    "data/processed/window_features_with_anomalies.csv"
)

summaries = []

for i, row in df.iterrows():

    print(f"Processing Window {i+1}/{len(df)}")

    summary = summarize(row)

    summaries.append(summary)

df["Summary"] = summaries

df.to_csv(
    "data/processed/final_summary.csv",
    index=False
)

print()

print("Finished!")

print("=" * 60)