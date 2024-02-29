import streamlit as st
from pycaret.regression import load_model, predict_model 
import pandas as pd 

modelo = load_model('model')
st.title("Inferir cantidad de anillos del Abalon")

shell_weight = st.number_input("Peso de la concha", help="Peso total de la concha en gramos")
viscera_weight = st.number_input("Peso de las vísceras", help="Peso total de las vísceras en gramos")
shucked_weight = st.number_input("Peso de la carne", help="Peso total de la carne en gramos")
whole_weight = st.number_input("Peso total", help="Peso total del abalon en gramos")
height = st.number_input("Altura", help="Altura del abalon en centímetros")
diameter = st.number_input("Diámetro", help="Diámetro del abalon en centímetros")
length = st.number_input("Longitud", help="Longitud del abalon en centímetros")
sex = st.number_input("Sexo (1, 2, 3)", help="Código que representa el sexo del abalon, 1= Macho, 2= Hembra, 3= Indeterminado")

if st.button("predecir"):
    input_data = pd.DataFrame([[shell_weight, viscera_weight, shucked_weight, whole_weight, height, diameter, length, sex]], columns=["shell-weight", "viscera-weight", "shucked-weight", "whole-weight", "height", "diameter", "length", "sex"])
    prediction = predict_model(modelo, data=input_data)
    st.write(prediction)