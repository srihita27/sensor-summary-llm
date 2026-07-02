def build_prompt(row):

    prompt = f"""
You are an Industrial IoT monitoring expert.

Analyze the following sensor statistics and produce a concise report.

Time Window:
{row['Start Time']} to {row['End Time']}

Temperature
Mean: {row['Temperature_Mean']:.2f}
Min: {row['Temperature_Min']:.2f}
Max: {row['Temperature_Max']:.2f}
Trend: {row['Temperature_Trend']}
Anomalies: {row['Temperature_Anomalies']}

Humidity
Mean: {row['Humidity_Mean']:.2f}
Trend: {row['Humidity_Trend']}
Anomalies: {row['Humidity_Anomalies']}

Pressure
Mean: {row['Pressure_Mean']:.2f}
Trend: {row['Pressure_Trend']}
Anomalies: {row['Pressure_Anomalies']}

CO2
Mean: {row['Co2 Gas_Mean']:.2f}
Trend: {row['Co2 Gas_Trend']}
Anomalies: {row['Co2 Gas_Anomalies']}

PM2.5
Mean: {row['PM2.5_Mean']:.2f}
Trend: {row['PM2.5_Trend']}
Anomalies: {row['PM2.5_Anomalies']}

PM10
Mean: {row['PM10_Mean']:.2f}
Trend: {row['PM10_Trend']}
Anomalies: {row['PM10_Anomalies']}

Generate a report with:

1. Overall conditions
2. Important trends
3. Anomalies
4. Recommendation

Keep it under 120 words.
"""

    return prompt