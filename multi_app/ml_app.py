import streamlit as st

# Load Machine Learning Packages
import joblib
import os

# Load EDA Packages
import numpy as np

attrib_info = """
#### Attribute Information:
    - Age 1.20-65
    - Sex 1. Male, 2.Female
    - Polyuria 1.Yes, 2.No.
    - Polydipsia 1.Yes, 2.No.
    - sudden weight loss 1.Yes, 2.No.
    - weakness 1.Yes, 2.No.
    - Polyphagia 1.Yes, 2.No.
    - Genital thrush 1.Yes, 2.No.
    - visual blurring 1.Yes, 2.No.
    - Itching 1.Yes, 2.No.
    - Irritability 1.Yes, 2.No.
    - delayed healing 1.Yes, 2.No.
    - partial paresis 1.Yes, 2.No.
    - muscle stiffness 1.Yes, 2.No.
    - Alopecia 1.Yes, 2.No.
    - Obesity 1.Yes, 2.No.
    - Class 1.Positive, 2.Negative.

"""
label_dict = {"No":0, "Yes": 1}
gender_map = {"Female":0, "Male":0}
target_label_map = {"Negative":0, "Positive":1}

def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache_data
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def ml_app():
    st.subheader("Machine Learning Prediction")
    # st.write("It is working")
    # st.success("Wow, this is cool")
    
    with st.expander("Attribute Info"):
        st.markdown(attrib_info)
        
    
    # Layout
    col1,col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", 10,100)
        gender = st.radio("Gender", ["Female", "Male"])
        polyuria = st.radio("Polyuria", ["Yes", "No"])
        polydipsia = st.radio("Polydipsia", ["Yes", "No"])
        sudden_weight_loss = st.selectbox("Sudden Weight Loss", ["Yes","No"])
        weakness = st.radio("Weakness", ["Yes", "No"])
        polyphagia = st.radio("Polyphagia",["Yes", "No"])
        genital_thrush = st.selectbox("Genital Thrush", ["Yes", "No"])
    
        
    with col2:
        visual_blurring = st.selectbox("Visual Blurring", ["Yes", "No"])
        itching = st.radio("Itching", ["Yes", "No"])
        irritability = st.radio("Irritability", ["Yes", "No"])
        delayed_healing = st.radio("Delayed Healing", ["Yes", "No"])
        partial_paresis = st.selectbox("Partial Paresis", ["Yes","No"])
        muscle_stiffness = st.radio("Muscle Stiffness", ["Yes", "No"])
        alopecia = st.radio("Alopecia", ["Yes", "No"])
        obesity = st.select_slider("Obesity", ["Yes", "No"])
        
        
    with st.expander("Your Selected Options"):
        result = {
        'Age':age,
		'Gender':gender,
		'Polyuria':polyuria,
		'Polydipsia':polydipsia,
		'Sudden Weight Loss':sudden_weight_loss,
		'Weakness':weakness,
		'Polyphagia':polyphagia,
		'Genital_thrush':genital_thrush,
		'Visual Blurring':visual_blurring,
		'Itching':itching,
		'Irritability':irritability,
		'Delayed Healing':delayed_healing,
		'Partial Paresis':partial_paresis,
		'Muscle Stiffness':muscle_stiffness,
		'Alopecia':alopecia,
		'Obesity':obesity
        }
        
        st.write(result)
        
        encoded_result = []
        for i in result.values():
            if type(i) == int:
                encoded_result.append(i)
            elif i in ["Female", "Male"]:
                res = get_value(i, gender_map)
                encoded_result.append(res)
            else:
                encoded_result.append(get_fvalue(i))
        
        st.write(encoded_result)
        
    
    with st.expander("Prediction Result"):
        single_sample = np.array(encoded_result).reshape(1, -1)
        # st.write(single_sample)
        
        model = load_model("models/logistic_regression_model_diabetes_21_oct_2020.pkl")
        prediction = model.predict(single_sample)
        pred_prob = model.predict_proba(single_sample)
        # st.write(prediction)
        # st.write(pred_prob)
        
        if prediction == 1:
            st.warning("Positive Risk {}".format(prediction[0]))
            pred_probability_score = {"Negative DM Risk": pred_prob[0][0]*100, "Positive DM Risk": pred_prob[0][1]*100}
            st.write(pred_probability_score)
        else:
            st.success("Negative Risk {}".format(prediction[0]))
            pred_probability_score = {"Negative DM Risk": pred_prob[0][0]*100, "Positive DM Risk": pred_prob[0][1]*100}
            st.write(pred_probability_score)
