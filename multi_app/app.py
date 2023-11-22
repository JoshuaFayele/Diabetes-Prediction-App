import streamlit as st
import streamlit.components.v1 as stc
import webbrowser

# Configure Streamlit page
from PIL import Image
img = Image.open("data/diabetes.png")
st.set_page_config(page_title='Diabetes Prediction App', page_icon=img)

# Import Mini Apps
from eda_app import run_eda_app
from ml_app import ml_app


html_temp = """
		<div style="background-color:#6c5b2e;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage Diabetes Risk Prediction App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""



def main():
    # st.title("Main App")
    stc.html(html_temp)
    
    menu = ["Home", "Exploratory Data Analysis", "Machine Learning", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice =="Home":
        st.subheader("Home")
        st.write("""
                    ### Early Stage Diabetes Risk Predictor App
                    This dataset contains the sign and symptoms data of newly diabetic patient.
                    #### Datasource
                        - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                    #### App Content
                        - Exploratory Data Analysis Section: Exploratory Data Analysis of Data
                        - Machine Learning Section: Machine Learning Predictor App
                    

                  
                """)
       
    elif choice == "Exploratory Data Analysis":
        run_eda_app()
    elif choice == "Machine Learning":
        ml_app()
    else:
        st.subheader("About this App")
        st.write("""
                 This app displays data from UC Irvine Machine Learning Repository.
                 #### Datasource
                        https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
                The purppose of this App is to predict early stages of diabetes using machine learning models. The prediction was done using Logistic regression. More research can be done to make the prediction of the model better and give better accuracy of result.      
                 
                    
                
                
                 """)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("X"):
                webbrowser.open("https://twitter.com/JoshuaFayele")
        with col2:
            if st.button("GitHub"):
                webbrowser.open("https://github.com/JoshuaFayele")
        with col3:
            if st.button("Email"):
                webbrowser.open("mailto:joshuafayele@gmail.com")
        with col4:
            if st.button("LinkedIn"):
                webbrowser.open("https://www.linkedin.com/in/joshuafayele/")
                
        # links = ["Twitter", "Github"]
        # for link in links:
        #     if link == "Twitter":
        #         webbrowser.open("https://github.com/JoshuaFayele")
        # st.button()
    
    
    
    
if __name__ == '__main__':
    main()