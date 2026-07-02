import pandas as pd
import numpy as np


class FeatureEngineer:

    def __init__(self, window_size=100):
        self.window_size = window_size

    def split_windows(self, df):
        """
        Split dataframe into fixed-size windows.
        """
        windows = []

        for i in range(0, len(df), self.window_size):
            window = df.iloc[i:i+self.window_size]

            if len(window) == self.window_size:
                windows.append(window)

        return windows

    def calculate_trend(self, series):

        x = np.arange(len(series))

        slope = np.polyfit(x, series, 1)[0]

        if slope > 0.01:
            return "Increasing"

        elif slope < -0.01:
            return "Decreasing"

        else:
            return "Stable"

    def extract_features(self, window):

        sensors = [
            "Temperature",
            "Humidity",
            "Pressure",
            "Co2 Gas",
            "PM2.5",
            "PM10"
        ]

        features = {}

        start_time = window["Datetime"].iloc[0]
        end_time = window["Datetime"].iloc[-1]

        features["Start Time"] = start_time
        features["End Time"] = end_time

        for sensor in sensors:

            features[f"{sensor}_Mean"] = window[sensor].mean()

            features[f"{sensor}_Min"] = window[sensor].min()

            features[f"{sensor}_Max"] = window[sensor].max()

            features[f"{sensor}_Std"] = window[sensor].std()

            features[f"{sensor}_Trend"] = self.calculate_trend(window[sensor])

        return features

    def generate_feature_dataframe(self, df):

        windows = self.split_windows(df)

        all_features = []

        for window in windows:
            all_features.append(self.extract_features(window))

        return pd.DataFrame(all_features)