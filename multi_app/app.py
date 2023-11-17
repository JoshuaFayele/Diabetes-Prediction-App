import streamlit as st
import streamlit.components.v1 as stc


# Import Mini Apps
from eda_app import run_eda_app
from ml_app import ml_app


html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""



def main():
    st.title("Main App")
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
        st.subheader("About")
    
    
    
    
if __name__ == '__main__':
    main()