# Financial-Fraud-Detection using PySpark & MLlib
Machine Learning project using PySpark &amp; Streamlit to detect financial fraud


A scalable solution for detecting fraudulent financial transactions using PySpark, MLlib, and a simple web interface for real-time prediction.

---

## 📝 Description

This project aims to identify fraudulent transactions from a financial dataset using **Machine Learning** techniques and **PySpark**. Built for Big Data environments, the system is efficient and scalable.

### 🔍 Key Features

1. **Data Preprocessing**: Cleaned large transaction dataset using PySpark.
2. **Fraud Classification**: Trained a **Random Forest Classifier** with high precision and recall.
3. **Model Evaluation**: Evaluated with AUC, precision, recall, and accuracy metrics.
4. **Feature Importance**: Identified most influential features (e.g., oldbalanceOrg, amount).
5. **Predictions Export**: Saved model predictions for visualization or dashboarding.
6. **Web App**: Deployed a simple **Flask**-based interface to upload transactions and check for fraud.

---

## 🚀 Built With

### 📌 Languages

* ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
* ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
* ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

### 🧰 Libraries & Frameworks

* ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apache-spark&logoColor=white) – Big data processing and ML model training
* ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) – Web app interface for fraud detection
* Pandas – Data manipulation
* Matplotlib – Visualizations

---

## 🛠️ Getting Started

### ✅ Prerequisites

- Python 3.10+
- Apache Spark & PySpark
- pip for installing packages
- Git (for cloning the repo)

### 🔧 Installation

```bash
git clone https://github.com/niyatipatel2005/financial-fraud-detection.git
cd financial-fraud-detection
pip install -r requirements.txt
```

## 📊 Running the Project

### 1. Train the Model

Run the main notebook or training script to preprocess the dataset and train the model using Random Forest:

```bash
# Inside your Jupyter Notebook or script
spark-submit fraud_detection_model.py
```

### 2. Launch the Web App

```bash
cd fraud_detection_dashboard
python app.py
```
Then open http://localhost:8501 in your browser to test fraud predictions by uploading CSV files.

## Authors

* Niyati Patel  -  https://github.com/niyatipatel2005


## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
