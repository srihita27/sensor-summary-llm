🤖 SensorGPT: LLM-Based Sensor Data Summarization
An AI-powered system that transforms raw IoT environmental sensor data into concise natural language summaries using data preprocessing, statistical feature engineering, anomaly detection, and a lightweight Large Language Model (LLM).

🚀 Features
📂 Sensor Data Preprocessing
📊 Statistical Feature Extraction
📈 Trend Detection
🚨 Z-Score Based Anomaly Detection
🤖 AI-Powered Sensor Data Summarization
📄 Automated Summary Generation
📌 Project Pipeline
Raw Sensor Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Anomaly Detection
        │
        ▼
Prompt Engineering
        │
        ▼
Lightweight LLM
        │
        ▼
Natural Language Summary
📁 Dataset
Dataset Source:

https://www.kaggle.com/datasets/yungbyun/sensor-data

The dataset contains:

Temperature
Humidity
Pressure
CO₂ Gas
PM2.5
PM10
Timestamp
Day/Night Indicator
🛠 Technologies Used
Python
Pandas
NumPy
SciPy
Scikit-learn
Transformers
Ollama
SmolLM2 / Qwen
📂 Project Structure
sensor-summary-llm/
│
├── data/
│   ├── raw/
│   └── processed/
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
├── PROJECT_OVERVIEW.md
├── ARCHITECTURE.md
├── requirements.txt
└── README.md
📊 Output
The system generates:

Cleaned Dataset
Window-based Features
Anomaly Statistics
AI Generated Environmental Summary
Example:

Temperature remained stable around 23°C with minimal humidity variation. CO₂ exhibited two minor spikes while PM2.5 and PM10 remained within acceptable limits. Overall environmental conditions remained stable.

🔮 Future Improvements
Streamlit Dashboard
Interactive Plotly Charts
ChatGPT-style Interface
PDF Report Generation
RAG Integration
Real-time IoT Monitoring
👨‍💻 Author
Made by Srihita Kotagiri | Developed as an AI-powered IoT Sensor Data Summarization project.
