# 📊 Customer Churn Prediction

This project predicts whether a customer will churn based on their personal and service-related data. It uses a trained machine learning pipeline (with preprocessing and logistic regression) and deploys an interactive web app using **Streamlit**.

---

## 🔍 About the Project

Customer churn is when a customer stops using a company’s services. This prediction tool helps telecom companies proactively identify customers at risk of leaving.

We used:
- A cleaned dataset with both numerical and categorical features
- Preprocessing using `OneHotEncoder` for categorical variables
- A `LogisticRegression` classifier
- A full pipeline built with `scikit-learn`
- Deployment using `Streamlit` for easy interaction

---

## 🧠 Model & Features

The model was trained using the following raw features:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Paperless Billing
- Monthly Charges
- Total Charges
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Payment Method

These were preprocessed with `OneHotEncoder` and passed into a `LogisticRegression` model.

---

## 🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- Streamlit
- joblib

---

## 📂 Project Structure

