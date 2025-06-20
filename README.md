# Early-Stage Diabetes Prediction App

An interactive machine learning web app that predicts the likelihood of early-stage diabetes based on user input and clinical symptom data.

## 🚀 Overview
This project combines data science, machine learning, and health analytics to create a predictive tool for early-stage diabetes. It features an interactive interface that enables users to explore real-world clinical data and get predictions based on medically relevant symptoms.

## 🔍 Features
- **Home**: Introduction and navigation
- **Exploratory Data Analysis (EDA)**:
  - Summary statistics and distributions
  - Class and gender breakdown
  - Visualizations: correlation heatmap, outliers, age frequency
- **Machine Learning Prediction**:
  - User selects symptoms
  - Model returns diabetes risk classification
- **About**:
  - App purpose, data source, and creator bio

## 🧪 Dataset
- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset)
- Features: Age, Gender, Polyuria, Polydipsia, Sudden Weight Loss, Weakness, Polyphagia, Genital Thrush, Visual Blurring, Itching, Irritability, Delayed Healing, Partial Paresis, Muscle Stiffness, Alopecia, Obesity
- Target: Class (Positive/Negative diabetes prediction)

## ⚙️ ML Pipeline
- Data Cleaning & Encoding
- Exploratory Data Analysis
- Feature Engineering
- Model Training & Evaluation (Logistic Regression, Decision Tree, Random Forest)
- Streamlit Integration for Deployment

## 📊 Results
- Achieved over 90% accuracy
- Real-time predictions based on user input
- Transparent model behavior through visualizations

## 📁 Folder Structure
```
├── data
│   └── diabetes.png
│   └── diabetes_data_upload.csv
│   └── diabetes_data_upload_clean.csv
│   └── freqdist_of_age_data.csv
├── models
│   └── decision_tree_model_diabetes_21_oct_2020.pkl
│   └── logistic_regression_model_diabetes_21_oct_2020.pkl
├── multi_app
│   └── app.py
│   └── eda_app.py
│   └── ml_app.py
│   └── st_functions.py
├── style.css
├── requirements.txt
└── README.md
```

## 🛠 Technologies Used
- Python (Pandas, NumPy, Scikit-learn)
- Streamlit
- Matplotlib, Seaborn

## 🧑‍💻 Developer
**Joshua Fayele**  
[LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/JoshuaFayele)  
Feel free to connect or reach out!

---

## 📜 License
This project is open source and available under the [MIT License](LICENSE).
