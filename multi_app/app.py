import streamlit as st

# Import Mini Apps
from eda_app import eda_app

def main():
    st.title("Main App")
    
    menu = ["Home", "Exploratory Data Analysis", "Machine Learning", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice =="Home":
        st.subheader("Home")
    elif choice == "Exploratory Data Analysis":
        pass
    elif choice == "Machine Learning":
        pass
    else:
        st.subheader("About")
    
    
    
    
if __name__ == '__main__':
    main()