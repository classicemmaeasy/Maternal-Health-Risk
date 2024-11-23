import streamlit as st
import pickle 
import numpy as np


loaded_model=pickle.load(open('C:/Users/HP/Documents/Preg/model_R.pkl', 'rb'))

sc_model=pickle.load(open('C:/Users/HP/Documents/Preg/sc_model (1).sav', 'rb'))



def preg_prediction(input_data):
    try:
        data_to_array= np.asarray(input_data)
        data_reshaped= data_to_array.reshape(1,-1)
        R_data=sc_model.transform(data_reshaped)
        prediction=loaded_model.predict(R_data)
        print(prediction)
    except ValueError:
        return "Please enter numbers only"

    if (prediction[0] == 0):
        return 'This patient has low risk pregnancy to issues'
    elif (prediction[0] == 1):
        return  'This patient has mid risk pregnancy issues'
    elif (prediction[0] == 2):
        return 'This patient has high risk pregnancy issues'
    else:
        return 'invalid dataset'


def main():


    
    st.title("Welcome to the Maternal Health Risk Prediction App😊")


    st.write("This app predicts the risk level for maternal health based on various factors.")


    
    #getting the input data  from the user
    Age= st.text_input('Enter Age')
    Systolic= st.text_input('Enter Systolic Blood Pressure')
    BS= st.text_input('Enter Blood Sugar')
    BT=st.text_input('Enter Body Temperature level')
    HR=st.text_input('Enter Heart Rate level')
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Pregnancy Risk Delivery Prediction:'):
        diagnosis= preg_prediction([Age,Systolic,BS,BT,HR])
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()