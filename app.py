import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model

# Cargar el modelo
modelo = load_model('model')

st.title("Inferir cantidad de anillos del Abalon")

# Definir los campos de entrada
shell_weight = st.number_input("Peso de la concha", help="Peso total de la concha en gramos")
viscera_weight = st.number_input("Peso de las vísceras", help="Peso total de las vísceras en gramos")
shucked_weight = st.number_input("Peso de la carne", help="Peso total de la carne en gramos")
whole_weight = st.number_input("Peso total", help="Peso total del abalon en gramos")
height = st.number_input("Altura", help="Altura del abalon en centímetros")
diameter = st.number_input("Diámetro", help="Diámetro del abalon en centímetros")
length = st.number_input("Longitud", help="Longitud del abalon en centímetros")
sex = st.selectbox("Sexo", options=["Macho", "Hembra", "Indeterminado"])

# Convertir el sexo a código numérico
sex_mapping = {"Macho": 1, "Hembra": 2, "Indeterminado": 3}
sex_code = sex_mapping[sex]

if st.button("Predecir"):
    # Crear un DataFrame con los datos de entrada
    input_data = pd.DataFrame([[shell_weight, viscera_weight, shucked_weight, whole_weight, height, diameter, length, sex_code]],
                              columns=["shell-weight", "viscera-weight", "shucked-weight", "whole-weight", "height", "diameter", "length", "sex"])
    # Realizar la predicción
    prediction = predict_model(modelo, data=input_data)
    # Mostrar la predicción
    st.write("Cantidad de anillos predichos:", int(prediction.Label[0]))