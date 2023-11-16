import streamlit as st

# Load EDA Packages
import pandas as pd

def eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.dataframe(df)