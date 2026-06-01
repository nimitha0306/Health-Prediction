# 🏥 Health Prediction Application

## Overview

The Health Prediction Application is a Python-based web application developed using Streamlit and SQLite. The application allows users to manage patient health records and predict potential health risks based on blood test results.

The system supports complete CRUD (Create, Read, Update, Delete) operations and automatically generates health remarks based on patient test values.

---

## Features

### Patient Information Management

* Full Name
* Date of Birth
* Email Address
* Glucose Level
* Haemoglobin Level
* Cholesterol Level
* AI-Generated Health Remarks

### CRUD Operations

* Create Patient Records
* View Patient Records
* Update Existing Records
* Delete Records

### Data Validation

* Valid Email Format Validation
* Date of Birth Cannot Be a Future Date
* Numeric Validation for Blood Test Values

### Health Prediction

The application analyzes:

* Glucose
* Haemoglobin
* Cholesterol

Based on these values, the system predicts possible health risks such as:

* High Diabetes Risk
* High Cholesterol Risk
* Possible Anemia
* Normal Health Indicators

### Persistent Storage

* SQLite Database
* Stores all patient records permanently

---

## Technologies Used

* Python 3.x
* Streamlit
* SQLite
* Pandas

---

## Project Structure

```text
health_prediction_app/
│
├── app.py
├── database.py
├── prediction.py
├── patients.db
├── requirements.txt
└── README.md
```

---

## Installation

git clone https://github.com/your-username/health-prediction-app.git
cd health-prediction-app
```

### Install Dependencies


pip install -r requirements.txt

streamlit run app.py
```

---

## Sample Patient Record

| Field         | Value                                               |
| ------------- | --------------------------------------------------- |
| Full Name     | John Smith                                          |
| Date of Birth | 1990-05-12                                          |
| Email         | [john.smith@gmail.com]|
| Glucose       | 165                                                 |
| Haemoglobin   | 11.5                                                |
| Cholesterol   | 220                                                 |

### Predicted Remarks

High Diabetes Risk
Possible Anemia
High Cholesterol Risk
