# Project Overview

## 1. Introduction

### Background

With the rapid growth of Internet of Things (IoT) technologies, environmental sensors continuously generate large volumes of real-time data. Monitoring parameters such as temperature, humidity, atmospheric pressure, carbon dioxide concentration, and particulate matter is essential for maintaining healthy and safe environments.

However, manually analyzing thousands of sensor readings is inefficient and often fails to provide quick, actionable insights.

SensorGPT addresses this challenge by combining statistical analysis, anomaly detection, and Large Language Models (LLMs) to automatically convert raw sensor readings into concise, human-readable reports.

---

## 2. Problem Statement

Traditional monitoring systems primarily visualize raw sensor values through graphs and dashboards. While useful, these systems still require users to manually interpret trends, detect anomalies, and understand the overall environmental conditions.

The objective of this project is to automate this interpretation process by generating intelligent natural language summaries from raw sensor data.

---

## 3. Project Objectives

The primary objectives of SensorGPT are to:

- Automate preprocessing of raw IoT sensor data
- Extract meaningful statistical features from time-series data
- Detect abnormal sensor behavior using anomaly detection techniques
- Generate concise natural language summaries using a lightweight Large Language Model
- Reduce manual effort involved in environmental data analysis

---

## 4. Dataset Description

### Dataset Source

Kaggle Dataset

https://www.kaggle.com/datasets/yungbyun/sensor-data

### Dataset Size

Approximately **4,100 sensor observations**

### Available Attributes

| Attribute | Description |
|-----------|-------------|
| ID | Unique sensor record identifier |
| Datetime | Timestamp of the reading |
| Temperature | Ambient temperature |
| Humidity | Relative humidity |
| Pressure | Atmospheric pressure |
| CO₂ Gas | Carbon dioxide concentration |
| PM2.5 | Fine particulate matter |
| PM10 | Coarse particulate matter |
| Daytime | Day / Night indicator |

---

# 5. System Workflow

The complete processing pipeline consists of four major stages.

```text
Raw Sensor Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Trend Detection
        │
        ▼
Anomaly Detection
        │
        ▼
Prompt Engineering
        │
        ▼
LLM-Based Summarization
        │
        ▼
Natural Language Report
```

---

# 6. Module Descriptions

---

## Module 1 — Data Preprocessing

### Purpose

Prepare the raw dataset for downstream statistical analysis.

### Operations Performed

- Removal of duplicate records
- Missing value handling
- Datetime conversion
- Chronological sorting
- Dataset validation

### Output

```
cleaned_sensor.csv
```

---

## Module 2 — Feature Engineering

### Purpose

Reduce thousands of sensor readings into meaningful statistical representations.

Instead of processing every individual reading, the dataset is divided into fixed-size windows of **100 observations**.

For every window, the following statistical descriptors are computed.

### Features Extracted

For each sensor:

- Mean
- Minimum
- Maximum
- Standard Deviation
- Trend

### Trend Categories

- Increasing
- Decreasing
- Stable

### Output

```
window_features.csv
```

---

## Module 3 — Anomaly Detection

### Purpose

Identify unusual sensor behavior before generating summaries.

### Technique Used

Z-Score Statistical Analysis

A sensor reading is classified as an anomaly when

```
|Z-score| > 3
```

Anomaly counts are computed independently for:

- Temperature
- Humidity
- Pressure
- CO₂ Gas
- PM2.5
- PM10

### Output

```
window_features_with_anomalies.csv
```

---

## Module 4 — LLM-Based Summarization

### Purpose

Convert structured statistical information into natural language.

Instead of providing raw numerical values to the language model, statistical features are transformed into structured prompts describing environmental conditions.

### Prompt Contents

Each prompt includes:

- Time window
- Statistical summaries
- Trend information
- Anomaly counts

### Generated Report

The LLM produces:

- Overall environmental conditions
- Significant trends
- Detected anomalies
- Monitoring recommendations

### Output

```
final_summary.csv
```

---

# 7. Processing Pipeline

```text
Raw Dataset
      │
      ▼
cleaned_sensor.csv
      │
      ▼
window_features.csv
      │
      ▼
window_features_with_anomalies.csv
      │
      ▼
Prompt Generation
      │
      ▼
Lightweight LLM
      │
      ▼
final_summary.csv
```

---

# 8. Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Statistical Analysis | SciPy |
| Machine Learning | Scikit-learn |
| LLM Framework | Transformers |
| Language Model | SmolLM2 / Qwen |
| Local Inference | Ollama |

---

# 9. Project Outputs

The system produces the following intermediate and final outputs.

| Output File | Description |
|------------|-------------|
| cleaned_sensor.csv | Cleaned dataset after preprocessing |
| window_features.csv | Window-level statistical features |
| window_features_with_anomalies.csv | Features with anomaly statistics |
| final_summary.csv | AI-generated natural language summaries |

---

# 10. Applications

SensorGPT can be applied in several real-world domains, including:

- Environmental Monitoring Systems
- Smart Buildings
- Industrial IoT
- Smart Manufacturing
- Air Quality Monitoring
- Indoor Climate Monitoring
- Smart Cities
- Research and Analytics

---

# 11. Current Limitations

Although the current implementation successfully summarizes historical sensor datasets, it has the following limitations:

- Supports offline CSV datasets only
- Does not process streaming sensor data
- No graphical dashboard in the current version
- Single-file batch processing
- Uses lightweight local language models

---

# 12. Future Enhancements

The project can be extended with several advanced capabilities:

- Interactive Streamlit dashboard
- Real-time sensor monitoring
- Plotly-based visual analytics
- ChatGPT-style conversational interface
- PDF report generation
- Retrieval-Augmented Generation (RAG)
- Multi-model LLM support
- Cloud deployment
- REST API for external integration

---

# 13. Conclusion

SensorGPT demonstrates a complete end-to-end pipeline for intelligent environmental sensor analysis. By integrating data preprocessing, statistical feature extraction, anomaly detection, prompt engineering, and lightweight Large Language Models, the system transforms raw numerical sensor readings into meaningful natural language summaries.

The project serves as a practical example of how Artificial Intelligence and Natural Language Processing can simplify the interpretation of IoT-generated data while significantly reducing manual analysis effort.
