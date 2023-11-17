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

def eda_app():
    st.subheader("From Exploratory Data Analysis")
    # df = pd.read_csv("data/diabetes_data_upload.csv")
    df = load_data("data/diabetes_data_upload.csv")
    # st.dataframe(df)
    df_encoded = load_data("data/diabetes_data_upload_clean.csv")
    freq_df = load_data("data/freqdist_of_age_data.csv")
    
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
            # Gender Distribution
            with st.expander("Distribution Plot of Gender"):
                # Using Seaborn
                #fig = plt.figure()
                #sns.countplot(df['Gender'])
                # sns.countplot(x ='Gender', data = df)
                # st.pyplot()
                # fig, ax = plt.subplots()
                # ax.scatter([1, 2, 3], [1, 2, 3])
                # st.pyplot(fig)
                fig = plt.figure()
                df['Gender'].value_counts().plot(kind='bar', color=['blue', 'orange'])
                st.pyplot(fig)
                
                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ["Gender Type", "Counts"]
                # st.dataframe(gen_df)
                
                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)
                
            # For Class Distribution
            with st.expander("Distribution Plot of Class"):
                fig = plt.figure()
                df['class'].value_counts().plot(kind='bar',  color=['blue', 'orange'])
                st.pyplot(fig)
                
        with col2:
            with st.expander("Gender Distribution"):
                st.dataframe(gen_df)
                
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())
        
        
        # Freq Dist
        with st. expander("Frequency Distribution of Age"):
            st.dataframe(freq_df)
            p2 = px.bar(freq_df, x='Age', y='count')
            st.plotly_chart(p2)
            
        # Outlier Detection
        with st.expander("Outlier Detection"):
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)
            
            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3)
        
        # Correlation
        with st.expander("Correlation Plot"):
            corr_matrix = df_encoded.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)
            
            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)
            