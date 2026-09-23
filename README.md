# AI-Powered Missing Person Investigation and Location Prediction System

An AI-powered web application that analyzes historical movement/trajectory data and predicts the possible location of a missing person based on learned movement patterns.

## 👨‍💻 Developer

**Sanu Kumar Singh**
B.Tech — Artificial Intelligence

---

## 📌 Project Overview

The **AI-Powered Missing Person Investigation and Location Prediction System** is a machine-learning-based application designed to assist in missing-person investigations.

The system processes historical GPS trajectory data, extracts movement-related features, trains a machine learning model, and predicts the possible geographical location of a missing person.

The project combines **Machine Learning, Data Analysis, Python, and Flask** to provide a web-based prediction interface.

---

## 🎯 Objectives

* Analyze historical GPS movement data.
* Identify movement patterns from trajectory data.
* Clean and preprocess GPS data.
* Extract useful features from geographical and temporal information.
* Train a machine learning model for location prediction.
* Evaluate the trained model using appropriate metrics.
* Provide a simple web interface for making predictions.
* Present prediction results in an understandable format.

---

## 🛠️ Technologies Used

* **Python**
* **Machine Learning**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Flask**
* **HTML**
* **CSS**
* **Matplotlib**
* **Git & GitHub**
* **Jupyter Notebook**

---

## 🧠 Machine Learning

The project uses a machine learning approach to learn relationships between movement-related features and geographical location.

### Data Processing

The GPS trajectory data was processed to create useful features such as:

* Latitude
* Longitude
* Altitude
* Timestamp
* Distance
* Time difference
* Speed
* Cleaned speed
* Hour
* Weekday
* Weekend indicator
* Movement indicator
* User ID

The data was cleaned and invalid/outlier speed values were handled before model training.

### Model

The trained model is used to predict the geographical location associated with the input movement information.

The trained deployment model is stored as:

```text
data/final_model/gps_location_prediction_deployment_model.pkl
```

The model is loaded using **Joblib** when the Flask application starts.

---

## 📊 Model Evaluation

The project includes model evaluation and analysis files such as:

* Final model metrics
* Model summary
* Feature importance
* Largest prediction errors
* Actual vs. predicted visualization
* Error distribution
* Accuracy/performance graph

These files are stored inside:

```text
data/final_results/
data/
```

---

## 🌐 Web Application

The project uses **Flask** to provide a web interface for the trained machine learning model.

### Main Components

```text
app/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── about.html
```

### Features

* Web-based interface
* User input for prediction
* Machine learning model integration
* Prediction result display
* About/project information page
* Custom CSS styling

---

## 📁 Project Structure

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
├── .gitignore
└── README.md
```

> Large raw datasets, processed datasets, virtual environments, and model files are excluded from Git using `.gitignore`.

---

## 📈 Project Workflow

```text
GPS Trajectory Data
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Saving
        ↓
Flask Web Application
        ↓
Location Prediction
```

---

## 📷 Application Screenshot

![Application Screenshot](screenshots/application-screenshot.png)

> Replace `application-screenshot.png` with the exact name of the screenshot stored in the `screenshots` folder.

---

## 🔍 Important Project Components

### 1. Data Collection

Historical GPS trajectory data is used as the basis for analyzing movement patterns.

### 2. Data Preprocessing

The collected GPS data is cleaned and transformed into a structured format suitable for machine learning.

### 3. Feature Engineering

Movement-related features such as distance, time difference, speed, hour, weekday, and movement status are generated.

### 4. Machine Learning

A machine learning model is trained using the processed trajectory data.

### 5. Model Evaluation

The model is evaluated using prediction metrics and visual analysis.

### 6. Deployment

The trained model is integrated into a Flask web application.

### 7. Prediction

The application accepts relevant input information and generates a predicted geographical location.

---

## 📊 Results and Analysis

The repository contains generated analysis files including:

* Feature importance
* Final model metrics
* Model summary
* Largest prediction errors
* Actual vs. predicted results
* Error distribution
* Accuracy/performance visualization

These files can be used to understand the performance and behavior of the trained model.

---

## 🔒 Data & GitHub

The project uses `.gitignore` to prevent large or unnecessary files from being uploaded to GitHub.

Excluded files/folders include:

```text
venv/
.venv/
data/raw/
data/processed/
*.pkl
*.joblib
*.h5
*.keras
.env
__pycache__/
.ipynb_checkpoints/
```

This keeps the GitHub repository smaller and avoids uploading large datasets and local environment files.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sanuksingh/AI-Powered-Missing-Person-Investigation-and-Location-Prediction-System.git
```

### 2. Open the Project

```bash
cd AI-Powered-Missing-Person-Investigation-and-Location-Prediction-System
```

### 3. Create/Activate Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If the virtual environment has not been created yet:

```powershell
python -m venv venv
```

Then activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Required Libraries

Install the libraries required by the project, for example:

```bash
pip install flask pandas numpy scikit-learn joblib matplotlib
```

### 5. Run the Flask Application

From the project root:

```bash
python app/app.py
```

The application will start on the local Flask server.

---

## 🧪 Development Tools

The project was developed using:

* Python
* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📚 Dataset

The project uses GPS trajectory data for movement analysis and machine learning.

The raw and processed datasets are intentionally excluded from the GitHub repository because of their large size.

---

## ⚠️ Disclaimer

This project is an academic/technical demonstration of machine learning-based location prediction.

Predicted locations should not be treated as confirmed real-world locations. Actual missing-person investigations require verified information and appropriate involvement of authorized authorities.

---

## 👨‍💻 Author

**Sanu Kumar Singh**

B.Tech — Artificial Intelligence

### Technologies Used

**Python • Machine Learning • Pandas • NumPy • Scikit-learn • Flask • HTML • CSS • Matplotlib • Git • GitHub**
