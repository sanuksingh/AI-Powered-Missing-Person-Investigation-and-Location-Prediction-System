# AI-Powered Missing Person Investigation and Location Prediction System

An end-to-end machine learning project that analyzes GPS trajectory data and predicts a person's **next geographical location** using **Random Forest Regression**.

The trained model is integrated into a **Flask web application** with an interactive **Leaflet.js map** for visualizing the current and predicted locations.

> **Project Type:** Machine Learning + Data Analysis + Web Application
> **Model:** Random Forest Regression
> **Application:** Flask
> **Map Visualization:** Leaflet.js + OpenStreetMap

---

## 📌 Project Overview

The **AI-Powered Missing Person Investigation and Location Prediction System** is a machine-learning-based prototype for analyzing human movement patterns using historical GPS trajectory data.

The system processes GPS trajectories, performs data cleaning and feature engineering, learns movement patterns using **Random Forest Regression**, and predicts the next latitude and longitude of a person based on their current and previous movement information.

The trained model is deployed through a Flask web application where users can provide GPS and movement-related information and receive a predicted next location.

The project can also serve as a technical foundation for broader applications such as tourist movement analysis, location intelligence, and investigation support.

> **Important:** The current implementation focuses on GPS trajectory analysis and next-location prediction. Real-time GPS collection, complete tourist verification, mobile integration, and national-scale deployment are outside the current prototype and are listed under future scope.

---

## 🎯 Problem Statement

> Develop a National Tourist Tracking and Verification System that identifies, verifies, and monitors domestic tourist movement to generate comprehensive tourism analytics and support evidence-based tourism planning.

This project implements the **GPS movement analysis and next-location prediction component** of that broader system.

The same movement-analysis approach can also be explored as a supporting technology for missing-person investigation, where historical movement patterns may help estimate a person's probable next location.

---

## 🎯 Objectives

* Analyze large-scale GPS trajectory data.
* Clean and preprocess raw GPS records.
* Identify movement-related patterns.
* Engineer geographical and temporal features.
* Predict the next geographical location.
* Evaluate prediction performance using geographical distance.
* Analyze machine-learning feature importance.
* Save the trained model for deployment.
* Deploy the model using Flask.
* Visualize current and predicted locations on an interactive map.

---

# 🧠 Machine Learning Approach

## Algorithm Used

### Random Forest Regression

The project uses **Random Forest Regression** to predict two continuous geographical values:

```text
Next Latitude
Next Longitude
```

Since latitude and longitude are continuous numerical values, the problem is treated as a **regression problem** rather than a classification problem.

---

## Why Random Forest Regression?

Random Forest was selected because it:

* Handles nonlinear relationships.
* Works well with structured/tabular data.
* Can work with multiple numerical features.
* Is relatively robust to noisy data.
* Provides feature-importance information.
* Works well with engineered GPS and movement features.

---

## 🌲 Model Configuration

The Random Forest model was configured as:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    max_depth=None
)
```

### Parameters

| Parameter       |         Value |
| --------------- | ------------: |
| Number of trees |           100 |
| Random state    |            42 |
| CPU workers     | All available |
| Maximum depth   |          None |

---

# 📊 Dataset

The project uses the **Microsoft Geolife GPS Trajectory Dataset** for movement analysis and model development.

The processed dataset contains approximately:

* **24.87 million GPS records**
* **182 users**

The trajectory data contains information such as:

* Latitude
* Longitude
* Altitude
* Timestamp
* Distance
* Time difference
* Speed
* User ID

The dataset is used to learn relationships between previous/current movement information and the next geographical location.

> **Dataset Note:** The Geolife dataset is a general GPS trajectory dataset and is not specifically a dataset of Indian tourists or missing persons.

---

# 🔧 Data Preprocessing

The raw GPS trajectory data was processed before machine-learning training.

Major preprocessing operations include:

1. GPS trajectory loading
2. Timestamp processing
3. Duplicate/invalid record handling
4. Distance calculation
5. Time-difference calculation
6. Speed calculation
7. Speed outlier detection
8. Clean speed generation
9. Hour extraction
10. Weekend identification
11. Previous-location generation
12. Next-location generation
13. Missing-value handling

These steps transform raw GPS trajectories into structured data suitable for machine-learning training.

---

# 🧩 Feature Engineering

The final machine-learning model uses **10 features**.

| Feature              | Description                          |
| -------------------- | ------------------------------------ |
| `latitude`           | Current latitude                     |
| `longitude`          | Current longitude                    |
| `previous_latitude`  | Previous GPS latitude                |
| `previous_longitude` | Previous GPS longitude               |
| `altitude`           | Current altitude                     |
| `clean_speed_kmh`    | Cleaned movement speed               |
| `distance_m`         | Distance from the previous GPS point |
| `time_diff_sec`      | Time difference between GPS points   |
| `hour`               | Hour of the day                      |
| `is_weekend`         | Weekend indicator                    |

### Target Variables

The model predicts:

```text
next_latitude
next_longitude
```

---

# 🔀 Train/Test Strategy

A **user-based train/test split** was used.

```text
Total Users    : 182
Training Users : 145
Testing Users  : 37
```

The user-based split helps evaluate the model on users whose trajectories were not included in the training set.

This approach also reduces the possibility of overly optimistic evaluation caused by having the same user's movement trajectories in both training and testing data.

---

# 📈 Model Results

The final model evaluation produced the following results:

| Metric                  |         Result |
| ----------------------- | -------------: |
| Mean Prediction Error   |    43,799.39 m |
| Median Prediction Error |        20.24 m |
| Minimum Error           |         0.03 m |
| Maximum Error           | 2,554,491.59 m |
| Within 10 m             |         31.89% |
| Within 50 m             |         68.37% |
| Within 100 m            |         76.99% |
| Within 500 m            |         88.80% |
| Within 1 km             |         90.88% |
| Within 5 km             |         93.25% |
| Within 10 km            |         93.99% |

## Result Interpretation

The median prediction error was approximately **20.24 meters**, while **90.88% of predictions were within 1 kilometer** of the actual next location.

The mean prediction error is considerably higher because some predictions produced extremely large geographical errors.

This indicates that while many predictions are geographically close to the actual next location, the model can occasionally produce significant outliers.

These extreme errors represent an important limitation of the current model and provide opportunities for future improvement.

---

# 🔍 Feature Importance

Feature importance was analyzed using the trained Random Forest model.

The major features included:

| Feature              | Approx. Importance |
| -------------------- | -----------------: |
| `previous_longitude` |            ~58.68% |
| `longitude`          |            ~39.84% |
| `latitude`           |             ~0.91% |
| `previous_latitude`  |             ~0.57% |

Other features had comparatively smaller importance in this particular model.

> **Note:** Feature importance indicates how useful a feature was to the trained model. It does not mean that the feature causally determines the prediction.

---

# 🌐 Web Application

The trained model is integrated into a **Flask web application**.

The application provides a simple interface where users can enter movement-related information and receive a predicted next geographical location.

## Input Features

The application accepts:

* Current latitude
* Current longitude
* Previous latitude
* Previous longitude
* Altitude
* Speed
* Distance
* Time difference
* Hour
* Weekend status

## Prediction Workflow

```text
User Input
    ↓
Flask Application
    ↓
Feature DataFrame
    ↓
Random Forest Model
    ↓
Predicted Latitude + Longitude
    ↓
Prediction Result
    ↓
Interactive Map
```

---

# 🗺️ Interactive Map

The web application uses **Leaflet.js** for geographical visualization.

The map can display:

* Current location
* Predicted next location
* Movement between locations
* Latitude and longitude information

This provides a visual representation of the prediction instead of displaying only numerical coordinates.

The map uses **OpenStreetMap-based map tiles**.

---

# 🛠️ Technologies Used

## Programming

* Python

## Data Processing

* Pandas
* NumPy
* PyArrow
* Parquet

## Machine Learning

* Scikit-learn
* Random Forest Regression

## Model Serialization

* Joblib

## Web Development

* Flask
* HTML
* CSS

## Mapping

* Leaflet.js
* OpenStreetMap

## Data Analysis & Visualization

* Jupyter Notebook
* Matplotlib

## Development Tools

* Visual Studio Code
* Python Virtual Environment
* Git
* GitHub

---

# 📁 Project Structure

The GitHub repository contains the lightweight project files and analysis outputs.

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
├── screenshots/
│   └── application-screenshot.png
│
├── .gitignore
└── README.md
```

> The exact screenshot filename may differ depending on the file you add to the `screenshots` folder.

---

# 🔄 Complete Project Workflow

```text
Microsoft Geolife GPS Dataset
            ↓
       Data Collection
            ↓
       Data Cleaning
            ↓
     GPS Preprocessing
            ↓
     Feature Engineering
            ↓
 Previous/Next Location Creation
            ↓
  User-Based Train/Test Split
            ↓
   Random Forest Regression
            ↓
      Model Evaluation
            ↓
   Feature Importance Analysis
            ↓
    Model Serialization
            ↓
     Flask Web Application
            ↓
    Location Prediction
            ↓
    Leaflet Map Visualization
```

---

# 📷 Application Screenshot

Add your application screenshot to the `screenshots` folder and display it here.

```markdown
![Application Screenshot](screenshots/application-screenshot.png)
```

Example:

![Application Screenshot](screenshots/application-screenshot.png)

> Replace `application-screenshot.png` with the exact filename of your screenshot.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sanuksingh/AI-Powered-Missing-Person-Investigation-and-Location-Prediction-System.git
```

## 2. Open the Project

```bash
cd AI-Powered-Missing-Person-Investigation-and-Location-Prediction-System
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Required Libraries

Install the libraries required by the application:

```bash
pip install flask pandas numpy scikit-learn joblib
```

Additional libraries may be required when reproducing the complete data-processing and analysis workflow.

---

# ▶️ Run the Application

The Flask application is located at:

```text
app/app.py
```

From the project root directory, run:

```bash
python app/app.py
```

The application will start on the local Flask server.

Open:

```text
http://127.0.0.1:5000
```

in your browser.

> **Model Note:** The trained deployment model is intentionally excluded from GitHub because of its file size. The model must be available locally at the path expected by `app/app.py` before running the application.

---

# 💾 Large Files and GitHub

Large files are intentionally excluded from this GitHub repository.

The `.gitignore` file excludes:

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

This includes:

* Raw GPS trajectory data
* Processed Parquet datasets
* Large trained model files
* Python virtual environment
* Temporary/cache files

The repository therefore contains the source code, analysis results, documentation, and other lightweight project files while keeping very large files outside GitHub.

---

# ⚠️ Current Limitations

The current prototype has several limitations:

1. The Geolife dataset is not specifically an Indian tourist dataset.
2. The model predicts the next GPS coordinate rather than an entire future route.
3. Some predictions produce very large geographical errors.
4. The application currently relies on manually entered GPS and movement information.
5. Live GPS collection from a mobile device is not currently implemented.
6. Full tourist identity verification is not implemented.
7. Real-time monitoring is not currently implemented.
8. National-scale deployment would require additional infrastructure, security, privacy controls, and validation.
9. Model performance may vary for movement patterns that differ significantly from the training data.

---

# 🚀 Future Scope

The system can be extended with:

* Real-time GPS tracking
* Mobile application integration
* Real-time location streaming
* Tourist registration and verification
* Route prediction
* Destination prediction
* Movement anomaly detection
* Tourism analytics dashboard
* Indian tourism-specific datasets
* Larger and more diverse trajectory datasets
* LSTM/GRU-based trajectory prediction
* Transformer-based trajectory prediction
* Cloud deployment
* Authentication and authorization
* Location-data privacy and anonymization
* Real-time alert generation

---

# 🔐 Privacy Considerations

GPS trajectory data can contain sensitive information about people's movements.

A real-world implementation should therefore consider:

* User consent
* Authentication
* Authorization
* Secure data storage
* Encryption
* Data anonymization
* Limited data retention
* Controlled access to location information

---

# 🎓 Academic Contribution

This project demonstrates an end-to-end machine-learning workflow:

```text
Large GPS Dataset
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Feature Importance
       ↓
Model Serialization
       ↓
Web Deployment
       ↓
Geographical Visualization
```

It combines:

* Data preprocessing
* Feature engineering
* Machine learning
* Model evaluation
* Model deployment
* Web development
* Geographical visualization

into a single working prototype.

---

# 📋 Project Status

### Completed Prototype

The current version includes:

* ✅ GPS trajectory preprocessing
* ✅ GPS movement analysis
* ✅ Feature engineering
* ✅ Previous/next location generation
* ✅ User-based train/test split
* ✅ Random Forest Regression
* ✅ Next-location prediction
* ✅ Model evaluation
* ✅ Feature importance analysis
* ✅ Model serialization
* ✅ Flask web application
* ✅ Leaflet interactive map
* ✅ Prediction visualization

---

# ⚠️ Disclaimer

This project is an **academic and technical prototype** demonstrating machine-learning-based GPS next-location prediction.

Predicted locations should **not be treated as confirmed real-world locations**. Actual missing-person investigations require verified information and appropriate involvement of authorized authorities.

---

# 👨‍💻 Author

## Sanu Kumar Singh

**B.Tech — Artificial Intelligence**

### Skills Demonstrated in This Project

* Python
* Machine Learning
* Data Preprocessing
* Feature Engineering
* Random Forest Regression
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML
* CSS
* Leaflet.js
* Matplotlib
* Git & GitHub
* Model Deployment

---

# ⭐ Conclusion

The **AI-Powered Missing Person Investigation and Location Prediction System** demonstrates how historical GPS trajectory data can be processed and used to build a machine-learning model for predicting future geographical movement.

The project goes beyond model training by integrating the trained model into a **Flask web application** and visualizing the predicted location using an **interactive Leaflet.js map**.

The current prototype provides a foundation for future work in **location intelligence, tourist movement analysis, and investigation-support systems**, with opportunities for real-time GPS integration, improved trajectory models, larger datasets, and stronger privacy and security mechanisms.
