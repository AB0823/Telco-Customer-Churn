# Customer Churn Prediction Dashboard

A Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, subscription details, and service usage patterns. The project includes Exploratory Data Analysis (EDA), an XGBoost classification model, SHAP explainability, and an interactive Streamlit dashboard.

# 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. Retaining existing customers is often more cost-effective than acquiring new ones. This project helps identify customers who are at high risk of churning so businesses can take proactive retention measures.

The model predicts churn probability using customer data such as:

- Contract type
- Internet service
- Monthly charges
- Tenure
- Tech support usage
- Payment method
- And more

# 🚀 Features
- 📊 Exploratory Data Analysis (EDA)
- 🤖 XGBoost Classification Model
- 🔍 SHAP Explainability
- 🌐 Interactive Streamlit Web App
- 📈 Churn Probability Prediction
- 💡 Business Retention Recommendations
- ⚙️ Scikit-learn Pipeline for preprocessing + model integration

# 🛠️ Tech Stack
Python, 
Pandas, 
NumPy, 
Scikit-learn, 
XGBoost, 
SHAP, 
Streamlit, 
Matplotlib, 
Seaborn

# 📂 Dataset

Dataset used: Telco Customer Churn Dataset

The dataset contains customer information including:

- Demographics
- Account details
- Service subscriptions
- Billing information
- Churn status

📊 Exploratory Data Analysis

The project includes:

- Churn distribution analysis
- KDE plots for:
  - Tenure
  - Monthly Charges
  - Average Monthly Spend
  - Customer behavior insights
    
Key Insights
- Customers with month-to-month contracts are more likely to churn.
- Higher monthly charges are associated with increased churn risk.
- Customers with longer tenure are less likely to churn.

# 🤖 Machine Learning Pipeline

The project uses a Scikit-learn Pipeline containing:

- Preprocessing
  - StandardScaler for numerical features
  - OneHotEncoder for categorical features
- Model
  - XGBoost Classifier
- Evaluation Metrics
  - Accuracy Score
  - Classification Report
  - SHAP Feature Importance

# 🔍 SHAP Explainability

SHAP (SHapley Additive exPlanations) is used to explain model predictions and identify the most important features influencing churn predictions.

The SHAP summary plot helps visualize:

- Which features increase churn probability
- Which features reduce churn probability
- Overall feature importance

# 🌐 Streamlit Dashboard

The Streamlit app allows users to:

- Input customer details
- Predict churn probability
- View churn risk status
- Get retention recommendations
Inspect entered customer data

# 📸 Screenshots

<img width="1918" height="857" alt="image" src="https://github.com/user-attachments/assets/20394a1a-d0e9-4e5c-8e76-cfd0744fe936" />



# 📈 Future Improvements

- Add CSV upload for bulk predictions
- Deploy using Streamlit Community Cloud
- Add customer segmentation
- Add advanced business analytics dashboard
- Improve model performance with hyperparameter tuning

# 🎯 Business Impact

This project can help businesses:

- Identify high-risk customers
 Reduce customer churn
- Improve customer retention strategies
- Increase customer lifetime value
