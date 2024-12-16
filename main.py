
import streamlit as st
import pickle
import numpy as np

# Load models
loaded_model = pickle.load(open('model_R.pkl', 'rb'))
sc_model = pickle.load(open('sc_model (1).sav', 'rb'))

# Prediction function
def preg_prediction(input_data):
    try:
        # Converting my  input data to array
        data_to_array = np.asarray(input_data)
        data_reshaped = data_to_array.reshape(1, -1)
        
        # Scale the data using the loaded scaler model
        R_data = sc_model.transform(data_reshaped)
        
        # Predict using the loaded model
        prediction = loaded_model.predict(R_data)
        
    except ValueError:
        return "Please enter valid numerical values only."
    
    # Interpreting my prediction result
    if prediction[0] == 0:
        return 'This patient is at low risk for pregnancy issues.'
    elif prediction[0] == 1:
        return 'This patient is at mid risk for pregnancy issues.'
    elif prediction[0] == 2:
        return 'This patient is at high risk for pregnancy issues.'
    else:
        return 'Invalid dataset or model prediction error.'

# Main function to handle Streamlit interface
def main():
    # Custom CSS to hide Streamlit branding and footer
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        img {visibility: hidden;}
        footer:after {content: ''; display: none;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.markdown('<p style="font-size:22px; font-weight:bold;">Welcome to the Maternal Health Risk Prediction App😊</p>', unsafe_allow_html=True)
    st.write("This app predicts the risk level for maternal health based on various factors.")

    # Hints for user inputs
    age_hint = "The age of the person in years. It should be a numeric value."
    systolic_bp_hint = "The systolic blood pressure value, typically ranging between 90-180."
    bs_hint = "Blood sugar level in mg/dL, usually ranging from 70-120 mg/dL."
    body_temp_hint = "Body temperature in degrees Fahrenheit. Normal range is around 98.6°F."
    heart_rate_hint = "The heart rate in beats per minute. Normal range is around 60-100 bpm."

    # User input fields
    Age = st.number_input('Age', min_value=1, max_value=100, value=30, help=age_hint)
    Systolic = st.number_input('Systolic BP', min_value=80, max_value=200, value=120, help=systolic_bp_hint)
    BS = st.number_input('Blood Sugar', min_value=5.0, max_value=20.0, value=7.0, help=bs_hint)
    BT = st.number_input('Body Temperature', min_value=96.0, max_value=105.0, value=98.0, help=body_temp_hint)
    HR = st.number_input('Heart Rate', min_value=50, max_value=120, value=70, help=heart_rate_hint)

    # Prediction button
    diagnosis = ''
    if st.button('Pregnancy Risk Delivery Prediction'):
        diagnosis = preg_prediction([Age, Systolic, BS, BT, HR])
    
    # Display result
    st.success(diagnosis)

# Run the app
if __name__ == '__main__':
    main()








# import streamlit as st
# import pickle 
# import numpy as np


# loaded_model=pickle.load(open('model_R.pkl', 'rb'))

# sc_model=pickle.load(open('sc_model (1).sav', 'rb'))



# def preg_prediction(input_data):
#     try:
#         data_to_array= np.asarray(input_data)
#         data_reshaped= data_to_array.reshape(1,-1)
#         R_data=sc_model.transform(data_reshaped)
#         prediction=loaded_model.predict(R_data)
#         print(prediction)
#     except ValueError:
#         return "Please enter numbers only"

#     if (prediction[0] == 0):
#         return 'This patient is at low risk to pregnancy issues'
#     elif (prediction[0] == 1):
#         return  'This patient is at mid risk to pregnancy issues'
#     elif (prediction[0] == 2):
#         return 'This patient is at high risk to pregnancy issues'
#     else:
#         return 'invalid dataset'


# def main():


#     import streamlit as st


#     st.markdown('<p style="font-size:24px; font-weight:bold;">Welcome to the Maternal Health Risk Prediction App😊</p>', unsafe_allow_html=True)


#     st.write("This app predicts the risk level for maternal health based on various factors.")


#     age_hint = "The age of the person in years. It should be a numeric value."
#     systolic_bp_hint = "The systolic blood pressure value, typically ranging between 90-180."
#     bs_hint = "Blood sugar level in mg/dL, usually ranging from 70-120 mg/dL."
#     body_temp_hint = "Body temperature in degrees Fahrenheit. Normal range is around 98.6°F."
#     heart_rate_hint = "The heart rate in beats per minute. Normal range is around 60-100 bpm."

#     Age= st.number_input('Age', min_value=1, max_value=100, value=30, help=age_hint)
#     Systolic= st.number_input('Systolic BP', min_value=80, max_value=200, value=120, help=systolic_bp_hint)
#     BS= st.number_input('Blood Sugar', min_value=5.0, max_value=20.0, value=7.0, help=bs_hint)
#     BT= st.number_input('Body Temperature', min_value=96.0, max_value=105.0, value=98.0, help=body_temp_hint)
#     HR= st.number_input('Heart Rate', min_value=50, max_value=120, value=70, help=heart_rate_hint)

#     #code for prediction
#     diagnosis=''
    
#     #creating a button for prediction
#     if st.button('Pregnancy Risk Delivery Prediction:'):
#         diagnosis= preg_prediction([Age,Systolic,BS,BT,HR])
    
#     st.success(diagnosis)
    
# if __name__=='__main__':
#     main()


