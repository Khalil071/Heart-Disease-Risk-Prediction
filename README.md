Heart Disease Risk Prediction

Project Overview

This project aims to predict the risk of heart disease based on various health indicators and lifestyle factors using machine learning models. The dataset consists of 70,000 records with 19 features. A Random Forest model is trained along with other models like Logistic Regression, Neural Networks, and SVM. The best-performing model is then deployed using a Flask API to allow predictions through Postman.

Project Workflow

Data Preprocessing & Cleaning

Exploratory Data Analysis (EDA)

Model Training (Random Forest and other models)

Model Evaluation & Error Analysis

Model Deployment using Flask API

Testing API with Postman

1. Data Preprocessing & Cleaning

The dataset is loaded from a CSV file and analyzed for missing values and inconsistencies.

Since all columns are numeric and there are no missing values, the dataset is ready for analysis.

Features are split into X (input features) and y (target variable: Heart_Risk).

The dataset is divided into training and testing sets using train_test_split().

2. Exploratory Data Analysis (EDA)

Analyzed the distribution of target labels and features.

Used Seaborn and Matplotlib to visualize correlations, trends, and patterns.

Investigated potential feature importance using correlation matrices.

3. Model Training

The Random Forest Classifier is trained with n_estimators=100.

Additional models trained for comparison:

Logistic Regression

Neural Network (MLP Classifier with two hidden layers)

Support Vector Machine (SVM)

Each model is evaluated using accuracy, classification report, and confusion matrix.

4. Model Evaluation & Error Analysis

Predictions are compared with actual values to analyze model performance.

Incorrect predictions are extracted and analyzed.

A count plot of misclassified instances is generated for further insights.

5. Model Deployment using Flask API

The trained Random Forest model is saved using pickle and stored in Google Drive.

A Flask application is created to serve the model.

The API provides an endpoint where users can submit feature values and receive heart disease risk predictions.

6. Testing API with Postman

The Flask API is tested using Postman by sending sample input data and verifying predictions.

The API can be integrated into other applications for real-world usage.

Installation & Setup

Prerequisites:

Python 3.8+

Libraries: pandas, numpy, seaborn, matplotlib, scikit-learn, flask, pickle

Running the Project:

Clone the repository:

git clone https://github.com/your-username/heart-risk-prediction.git
cd heart-risk-prediction

Install required dependencies:

pip install -r requirements.txt

Run the Flask API:

python app.py

Use Postman or cURL to send requests to http://127.0.0.1:5000/predict.

Future Improvements

Optimize model performance using hyperparameter tuning.

Deploy the model on cloud platforms like AWS/GCP.

Integrate a front-end UI for better user experience.

Extend API to accept batch predictions.

Author

Khalil Samir

AI & Data Science Enthusiast

Feel free to contribute or raise issues in the repository!

