import streamlit as st

# Load EDA Packages
import pandas as pd

# Load Data Vizualization Package
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

# Load Data
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df


def debugger():
    st.subheader("From Exploratory Data Analysis")
    # df = pd.read_csv("data/diabetes_data_upload.csv")
    df = load_data("data/diabetes_data_upload.csv")
    # st.dataframe(df)
    df_encoded = load_data("data/diabetes_data_upload_clean.csv")
    
    submenu = st.sidebar.selectbox("Sub Menu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)
        
        with st.expander("Data Types"):
            st.dataframe(df.dtypes)
        
        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe())
        
        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())
        
        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())
        
    elif submenu == "Plots":
        st.subheader("Plots")
        
        # Layouts
        col1, col2 = st.columns([2,1])
        
        with col1:
            with st.expander("Distribution Plot of Gender"):
                # Using Seaborn
                fig = plt.figure()
                sns.countplot(df['Gender'])
                st.pyplot(fig)
    
if __name__ == '__debugger__':
    debugger()