import pandas as pd

from sklearn.preprocessing import StandardScaler


def load_dataset(path):
    """
    Load sensor dataset.
    """
    return pd.read_csv(path)


def clean_dataset(df):
    """
    Clean and preprocess the dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df = df.ffill()

    # Convert Datetime column
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Sort by timestamp
    df = df.sort_values("Datetime")

    # Reset index
    df = df.reset_index(drop=True)

    return df


def normalize_sensor_columns(df):

    sensor_cols = [
        "Temperature",
        "Humidity",
        "Pressure",
        "Co2 Gas",
        "PM2.5",
        "PM10"
    ]

    scaler = StandardScaler()

    df_scaled = df.copy()

    df_scaled[sensor_cols] = scaler.fit_transform(df[sensor_cols])

    return df_scaled


def save_dataset(df, path):

    df.to_csv(path, index=False)