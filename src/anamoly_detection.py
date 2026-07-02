import pandas as pd
import numpy as np
from scipy.stats import zscore


class AnomalyDetector:

    def __init__(self, threshold=3):
        self.threshold = threshold

    def detect(self, window):

        sensors = [
            "Temperature",
            "Humidity",
            "Pressure",
            "Co2 Gas",
            "PM2.5",
            "PM10"
        ]

        result = {}

        for sensor in sensors:

            values = window[sensor]

            z_scores = np.abs(zscore(values))

            anomalies = np.sum(z_scores > self.threshold)

            result[f"{sensor}_Anomalies"] = int(anomalies)

        return result