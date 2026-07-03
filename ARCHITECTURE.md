# System Architecture

## 1. Introduction

This document describes the architecture of **SensorGPT**, an AI-powered sensor data summarization system. The system processes environmental IoT sensor data through multiple stages, including preprocessing, statistical feature extraction, anomaly detection, prompt engineering, and Large Language Model (LLM) based summarization.

The architecture is modular, allowing each component to operate independently while maintaining a sequential data processing pipeline.

---

# 2. High-Level Architecture

```text
                         +-------------------------+
                         |   Raw Sensor Dataset    |
                         |      (CSV File)         |
                         +-----------+-------------+
                                     |
                                     |
                                     ▼
                  +--------------------------------------+
                  |     Data Preprocessing Module        |
                  |--------------------------------------|
                  | • Remove Duplicates                 |
                  | • Handle Missing Values             |
                  | • Convert Timestamps                |
                  | • Chronological Sorting             |
                  +----------------+---------------------+
                                   |
                                   ▼
                 +---------------------------------------+
                 |     Feature Engineering Module        |
                 |---------------------------------------|
                 | • Window Creation                     |
                 | • Mean                                |
                 | • Min / Max                           |
                 | • Standard Deviation                  |
                 | • Trend Detection                     |
                 +----------------+----------------------+
                                  |
                                  ▼
                 +---------------------------------------+
                 |     Anomaly Detection Module          |
                 |---------------------------------------|
                 | • Z-Score Analysis                    |
                 | • Outlier Identification              |
                 | • Anomaly Counting                    |
                 +----------------+----------------------+
                                  |
                                  ▼
                 +---------------------------------------+
                 |      Prompt Engineering Module        |
                 |---------------------------------------|
                 | Convert numerical statistics into     |
                 | structured prompts for the LLM.       |
                 +----------------+----------------------+
                                  |
                                  ▼
                 +---------------------------------------+
                 |     Lightweight Large Language Model  |
                 |---------------------------------------|
                 | SmolLM2 / Qwen / Ollama               |
                 | Natural Language Generation           |
                 +----------------+----------------------+
                                  |
                                  ▼
                 +---------------------------------------+
                 |      AI Generated Summary Report      |
                 |---------------------------------------|
                 | final_summary.csv                     |
                 +---------------------------------------+
```
<img width="1536" height="1024" alt="ChatGPT Image Jul 3, 2026, 08_44_25 AM (1)" src="https://github.com/user-attachments/assets/ba46e222-cd5c-4784-95c2-49a0b36931d8" />

---

# 3. System Workflow

The complete workflow of SensorGPT is illustrated below.

```text
                     Sensor Dataset
                            │
                            ▼
                  Data Preprocessing
                            │
                            ▼
                 Statistical Feature Extraction
                            │
                            ▼
                    Trend Identification
                            │
                            ▼
                    Anomaly Detection
                            │
                            ▼
                   Prompt Construction
                            │
                            ▼
               Lightweight Language Model
                            │
                            ▼
             Natural Language Summary Report
```

---

# 4. Module Architecture

The project is organized into independent modules, each responsible for a specific stage of the processing pipeline.

```text
                    SensorGPT

                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼

Data Preprocessing              Feature Engineering

        │                                 │
        └──────────────┬──────────────────┘
                       ▼

              Anomaly Detection

                       │
                       ▼

              Prompt Engineering

                       │
                       ▼

           Lightweight LLM Inference

                       │
                       ▼

          Natural Language Summary
```

---

# 5. Data Processing Pipeline

Each stage produces an intermediate output used by the subsequent module.

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

# 6. Directory Structure

```text
sensor-summary-llm/
│
├── data/
│   ├── raw/
│   │      sensor_data.csv
│   │
│   └── processed/
│          cleaned_sensor.csv
│          window_features.csv
│          window_features_with_anomalies.csv
│          final_summary.csv
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── anomaly_detection.py
│   ├── prompt_template.py
│   ├── summarizer.py
│   └── llm_loader.py
│
├── summarize_main.py
├── README.md
├── PROJECT_OVERVIEW.md
├── ARCHITECTURE.md
└── requirements.txt
```

---

# 7. Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| preprocessing.py | Cleans and prepares raw sensor data |
| feature_engineering.py | Computes statistical features for each window |
| anomaly_detection.py | Detects abnormal sensor readings using Z-Score |
| prompt_template.py | Generates structured prompts for the language model |
| summarizer.py | Sends prompts to the LLM and generates summaries |
| llm_loader.py | Loads and initializes the lightweight language model |

---

# 8. Technology Architecture

```text
                        Python

                           │
      ┌────────────────────┼─────────────────────┐
      ▼                    ▼                     ▼

   Pandas               NumPy              Scikit-learn

      │                    │                     │
      └────────────────────┼─────────────────────┘
                           ▼

                Statistical Feature Extraction

                           │
                           ▼

                   SciPy (Z-Score Analysis)

                           │
                           ▼

                  Prompt Engineering Module

                           │
                           ▼

             SmolLM2 / Qwen / Ollama LLM

                           │
                           ▼

             AI Generated Sensor Summary
```

---

# 9. Data Flow Diagram

<img width="1024" height="1536" alt="ChatGPT Image Jul 3, 2026, 08_44_25 AM (2)" src="https://github.com/user-attachments/assets/ac91dacc-7e3f-4498-ab1c-cde5fbd93815" />


# 10. Design Principles

The architecture follows the following software engineering principles:

- **Modular Design** – Each processing stage is implemented as an independent Python module.
- **Sequential Processing Pipeline** – Output from one module serves as input to the next.
- **Scalability** – New anomaly detection algorithms or language models can be integrated with minimal code changes.
- **Maintainability** – Components are loosely coupled and easy to extend.
- **Reusability** – Individual modules can be reused independently in future IoT analytics projects.

---

# 11. Current Architecture Limitations

The current implementation has the following constraints:

- Processes historical CSV datasets only.
- Supports batch processing rather than streaming data.
- Uses lightweight local LLMs for inference.
- Does not include a graphical user interface.
- Generates summaries one dataset at a time.

---

# 12. Planned Architecture Enhancements

Future versions of SensorGPT will extend the current architecture by incorporating:

<img width="1536" height="1024" alt="ChatGPT Image Jul 3, 2026, 08_44_26 AM (4)" src="https://github.com/user-attachments/assets/c1037bc0-ae37-4b81-b4d4-a452a7acb487" />


Future enhancements include:

- Interactive Streamlit dashboard
- Plotly visual analytics
- ChatGPT-style conversational interface
- Retrieval-Augmented Generation (RAG)
- Real-time IoT sensor monitoring
- PDF report generation
- REST API integration
- Cloud deployment

---

# 13. Architecture Summary

SensorGPT follows a modular AI pipeline that transforms raw IoT sensor readings into meaningful natural language summaries. By separating preprocessing, feature engineering, anomaly detection, prompt engineering, and LLM inference into independent components, the system remains scalable, maintainable, and easy to extend for future real-time IoT analytics applications.
