# 🤖 SensorGPT: LLM-Based Sensor Data Summarization

<p align="center">

**Transforming raw IoT sensor data into intelligent, human-readable insights using AI and Large Language Models (LLMs).**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

## 📖 Overview

SensorGPT is an AI-powered system that transforms raw environmental IoT sensor data into concise natural language summaries.

Instead of manually analyzing thousands of sensor readings, SensorGPT automatically:

- 📂 Cleans and preprocesses sensor data
- 📊 Extracts meaningful statistical features
- 📈 Detects sensor trends
- 🚨 Identifies anomalies using statistical methods
- 🤖 Generates AI-powered summaries using a lightweight Large Language Model (LLM)

---

# 🚀 Features

| Feature | Description |
|---------|-------------|
| 📂 Data Preprocessing | Cleans and prepares raw sensor data |
| 📊 Feature Engineering | Extracts statistical features from sensor readings |
| 📈 Trend Detection | Detects increasing, decreasing, or stable sensor behavior |
| 🚨 Anomaly Detection | Identifies abnormal readings using Z-Score analysis |
| 🤖 LLM Summarization | Converts sensor statistics into natural language summaries |
| 📄 Summary Generation | Produces concise environmental reports |

---

# 📌 Project Pipeline

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
              Trend Identification
                         │
                         ▼
               Anomaly Detection
                         │
                         ▼
              Prompt Engineering
                         │
                         ▼
             Lightweight LLM
        (SmolLM2 / Qwen / Ollama)
                         │
                         ▼
          Natural Language Summary
```

---

# 📁 Dataset

**Dataset Source**

🔗 https://www.kaggle.com/datasets/yungbyun/sensor-data

### Dataset Attributes

| Sensor |
|---------|
| 🌡 Temperature |
| 💧 Humidity |
| 🌍 Pressure |
| 🌫 CO₂ Gas |
| 🌬 PM2.5 |
| 🌬 PM10 |
| 🕒 Timestamp |
| 🌞 Day/Night Indicator |

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Statistical Analysis | SciPy |
| Machine Learning | Scikit-learn |
| LLM Framework | Transformers |
| Language Model | SmolLM2 / Qwen |
| Local Inference | Ollama |

---

# 📂 Project Structure

```text
sensor-summary-llm/
│
├── data/
│   ├── raw/
│   │     └── sensor_data.csv
│   │
│   └── processed/
│         ├── cleaned_sensor.csv
│         ├── window_features.csv
│         ├── window_features_with_anomalies.csv
│         └── final_summary.csv
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
├── requirements.txt
├── README.md
├── PROJECT_OVERVIEW.md
└── ARCHITECTURE.md
```

---

# 📊 Project Workflow

```text
Raw Sensor Data
        │
        ▼
Cleaning & Preprocessing
        │
        ▼
Feature Extraction
        │
        ▼
Trend Detection
        │
        ▼
Anomaly Detection
        │
        ▼
Prompt Generation
        │
        ▼
LLM Summarization
        │
        ▼
Generated Report
```

---

# 📄 Outputs

The project generates the following outputs:

- ✅ Cleaned Dataset
- ✅ Window-based Statistical Features
- ✅ Anomaly Detection Results
- ✅ AI-generated Sensor Summary

### Example Summary

> **Temperature remained stable around 23°C with minimal humidity variation. CO₂ exhibited two minor spikes while PM2.5 and PM10 remained within acceptable limits. Overall environmental conditions remained stable, and continued monitoring is recommended.**

---

# 🌍 Applications

SensorGPT can be applied in:

- 🏭 Industrial IoT Monitoring
- 🏢 Smart Buildings
- 🌆 Smart Cities
- 🌱 Environmental Monitoring
- 🌬 Air Quality Analysis
- 🏥 Indoor Climate Monitoring
- ⚙ Manufacturing Facilities

---

# 🔮 Future Improvements

- 🌐 Interactive Streamlit Dashboard
- 📈 Plotly-based Visualizations
- 💬 ChatGPT-style AI Interface
- 📄 PDF Report Generation
- 🔍 Retrieval-Augmented Generation (RAG)
- ☁ Cloud Deployment
- 📡 Real-time Sensor Data Monitoring

---

# 📸 Architecture

For detailed system design and workflow diagrams, refer to:

- 📄 **PROJECT_OVERVIEW.md**
- 🏗 **ARCHITECTURE.md**

---

# 👩‍💻 Author

**Srihita Kotagiri**

Computer Science Undergraduate | AI & Software Development Enthusiast

---

<p align="center">

⭐ If you found this project interesting, consider giving it a star!

</p>
