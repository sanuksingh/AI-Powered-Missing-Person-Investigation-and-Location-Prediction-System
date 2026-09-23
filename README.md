# AI-Powered Missing Person Investigation and Location Prediction System

An AI-powered system designed to analyze GPS trajectory data, understand movement patterns, and predict probable locations to support missing-person investigation.

## 📌 Project Overview

The **AI-Powered Missing Person Investigation and Location Prediction System** uses GPS trajectory data and machine learning techniques to analyze movement behavior and estimate probable future locations.

The system processes historical GPS trajectories, performs data cleaning and movement analysis, and provides location predictions through a web-based Flask application.

## 🎯 Problem Statement

Finding a missing person can be difficult when investigators have limited information about the person's recent movements.

This project aims to:

* Analyze historical GPS trajectory data
* Identify movement patterns
* Clean and preprocess GPS data
* Detect abnormal GPS/speed values
* Extract useful movement features
* Predict probable locations
* Display results through a web interface

## ✨ Key Features

* 📍 GPS trajectory data processing
* 🧹 Data cleaning and preprocessing
* 🚗 Movement and speed analysis
* ⚠️ GPS speed outlier detection
* 🤖 Machine learning-based location prediction
* 📊 Prediction performance analysis
* 🗺️ Map-based visualization
* 🌐 Flask web application
* 📈 Feature importance analysis
* 📉 Actual vs predicted analysis
* 📊 Error distribution analysis

## 🛠️ Technologies Used

| Technology       | Purpose              |
| ---------------- | -------------------- |
| Python           | Core programming     |
| Pandas           | Data processing      |
| NumPy            | Numerical operations |
| Scikit-learn     | Machine learning     |
| Flask            | Web application      |
| Folium / Leaflet | Map visualization    |
| Jupyter Notebook | Data analysis        |
| HTML             | Web interface        |
| CSS              | UI styling           |
| Git & GitHub     | Version control      |

## 📂 Project Structure

```text
AI-Powered-Missing-Person-Investigation-and-Location-Prediction-System/
│
├── app/
│   ├── app.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       └── about.html
│
├── data/
│   ├── final_model/
│   │   └── model_info.json
│   │
│   ├── final_results/
│   │   ├── final_model_results.csv
│   │   └── project_information.csv
│   │
│   ├── step65_largest_errors.csv
│   ├── step66_feature_importance.csv
│   ├── step66_feature_importance.png
│   ├── step67_final_metrics.csv
│   ├── step67_model_summary.csv
│   ├── step68_accuracy_graph.png
│   ├── step68_actual_vs_predicted.png
│   └── step68_error_distribution.png
│
├── notebooks/
│   └── 01_data_collection.ipynb
│
├── reports/
│
├── src/
│
├── .gitignore
└── README.md
```

## 🔄 System Workflow

```text
GPS Trajectory Data
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Outlier Detection
        ↓
Feature Engineering
        ↓
Movement Analysis
        ↓
Machine Learning Model
        ↓
Location Prediction
        ↓
Flask Web Application
        ↓
Predicted Location
```

## 🧹 Data Preprocessing

The GPS trajectory data goes through several preprocessing steps:

1. Remove invalid GPS records
2. Handle duplicate records
3. Convert timestamps
4. Calculate distance between GPS points
5. Calculate time differences
6. Calculate movement speed
7. Detect abnormal speed values
8. Handle speed outliers
9. Extract time-based features
10. Identify movement and stationary periods

## 📊 Model Evaluation

The project includes several evaluation and analysis outputs:

* Model performance metrics
* Feature importance
* Largest prediction errors
* Actual vs predicted visualization
* Error distribution
* Model summary

These outputs are stored inside the `data/` directory.

## 🌐 Web Application

The project includes a **Flask-based web application** that provides a user interface for the location prediction system.

To run the application:

```bash
python app/app.py
```

The application can then be accessed through the local Flask server.

## 📦 Dataset

This project uses GPS trajectory data for movement analysis.

The original and processed datasets are **not included in this GitHub repository** because of their large file size.

The following directories are intentionally excluded using `.gitignore`:

```text
data/raw/
data/processed/
```

Large trained model files such as `.pkl` are also excluded.

## 🔐 Large Files and GitHub

Large datasets and trained model binaries are kept locally and are not committed to GitHub.

This keeps the repository lightweight and makes it easier to clone and manage.

## 🚀 Future Scope

Possible future improvements include:

* Real-time GPS tracking
* Mobile application
* Real-time location updates
* More advanced trajectory prediction models
* Integration with emergency services
* Location confidence scoring
* Multiple-person trajectory analysis
* Cloud deployment
* Secure investigator dashboard
* Real-time alert generation

## 👨‍💻 Developer

**Sanu Kumar Singh**

B.Tech — Artificial Intelligence

### Skills Used

* Python
* Data Structures & Algorithms with Java
* Machine Learning
* Flask
* Streamlit
* Git & GitHub
* Data Analysis

## ⭐ Project Purpose

This project demonstrates the application of **Artificial Intelligence, Machine Learning, GPS trajectory analysis, and web development** to a real-world investigation and location prediction problem.
