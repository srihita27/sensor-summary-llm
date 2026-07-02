from config import *

from src.preprocessing import *

from src.utils import *

create_directories()

print("=" * 50)

print("Loading Dataset...")

df = load_dataset(RAW_DATA)

print(df.head())

print()

print("Dataset Shape:", df.shape)

print()

print("Cleaning Dataset...")

df = clean_dataset(df)

save_dataset(df, PROCESSED_DATA)

print()

print("Saved cleaned dataset to")

print(PROCESSED_DATA)

print("=" * 50)