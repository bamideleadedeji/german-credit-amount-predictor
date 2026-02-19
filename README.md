German Credit Amount Predictor
Project Overview
This project develops a machine learning solution to predict the recommended credit amount for bank customers. Using the German Credit Dataset, I built a regression pipeline that analyzes applicant demographics and financial history to provide data-driven loan estimates.

The final model is deployed as an interactive web application via Streamlit Cloud, allowing stakeholders to input customer profiles and receive real-time predictions.

Live Demo
View the interactive app here: 

The Machine Learning Pipeline
1. Data Preprocessing & EDA
Feature Engineering: Handled categorical variables using One-Hot Encoding (converting attributes like 'Purpose' and 'Housing' into numerical format).

Scaling: Applied StandardScaler to normalize numerical features (Age, Duration, Job level), ensuring the model is not biased toward large numerical values.

Analysis: Identified that loan Duration and Age were the strongest predictors of credit amount.

2. Modeling
Algorithm: Random Forest Regressor.

Why this model? Random Forests excel at capturing non-linear relationships in financial data and provide high robustess against outliers.

Persistence: The final model and scaler were serialized using joblib for seamless deployment.

3. Deployment
Framework: Streamlit.

Infrastructure: Hosted on Streamlit Cloud, pulling directly from the master branch of this GitHub repository.

Key Results
Top Predictors: Loan Duration, Age, and Housing Status.

Model Performance: The model successfully captures the variance in credit limits, providing a baseline for automated credit limit suggestions.

Repository Structure
streamlit_app.py: The main Python script for the web application.

credit_model.pkl: The trained Random Forest model.

scaler.pkl: The saved StandardScaler object.

requirements.txt: List of dependencies for cloud deployment.

master branch: The primary deployment branch.

How to Run Locally
Clone the repo: git clone [https://github.com/bamideleadedeji/german-credit-amount-predictor]

Install dependencies: pip install -r requirements.txt

Run the app: streamlit run streamlit_app.py

Contact
Your Name [https://www.linkedin.com/in/adedeji-bamidele-88a159263/] | [bamideleadedeji2000@gmail.com]
