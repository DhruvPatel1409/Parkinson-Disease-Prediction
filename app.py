import streamlit as st
import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/ADMIN/Desktop/vs code/streamlit/project6/parkinson_model.pkl','rb'))

def parkinson_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return 'The person is not having parkinson disease'
    else:
        return 'The person is having parkinson disease'

def main():

    st.title("PARKINSON DISEASE PREDICTOR")

    Fo = st.text_input("Enter your Average vocal fundamental frequency : ")
    Fhi = st.text_input("Enter your Maximum vocal fundamental frequency : ")
    Flo = st.text_input("Enter your  Minimum vocal fundamental frequency : ")
    Jitter_per = st.text_input("Enter your MDVP_Jitter(%) : ")
    Jitter_abs = st.text_input("Enter your MDVP_Jitter(Abs) : ")
    RAP = st.text_input("Enter your MDVP_RAP : ")
    PPQ = st.text_input("Enter your MDVP_PPQ : ")
    DDP = st.text_input("Enter your Jitter_DDP : ")
    Shimmer = st.text_input("Enter your MDVP_Shimmer : ")
    Shimmer_db = st.text_input("Enter your MDVP_Shimmer(dB) : ")
    APQ3 = st.text_input("Enter your Shimmer_APQ3 : ")
    APQ5 = st.text_input("Enter your Shimmer_APQ5 : ")
    APQ = st.text_input("Enter your MDVP_APQ : ")
    DDA = st.text_input("Enter your  Shimmer_DDA  : ")
    NHR = st.text_input("Enter your NHR : ")
    HNR = st.text_input("Enter your HNR : ")
    RPDE = st.text_input("Enter your RPDE : ")
    DFA = st.text_input("Enter your DFA : ")
    spread1 = st.text_input("Enter your spread1 : ")
    spread2 = st.text_input("Enter your spread2 : ")
    D2 = st.text_input("Enter your D2 : ")
    PPE = st.text_input("Enter your PPE : ")
   
    diagnosis = ' '

    if st.button('PREDICT'):
        diagnosis = parkinson_prediction([Fo,Fhi,Flo,Jitter_per,Jitter_abs,RAP,PPQ,DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()

