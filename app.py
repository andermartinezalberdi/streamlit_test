import streamlit as st
import random

st.title("Simulador de tirada de moneda")

st.write("Haz clic en el botón para tirar la moneda:")

if st.button("Tirar moneda"):
    resultado = random.choice(["Cara", "Cruz"])
    st.write(f"Resultado: **{resultado}**")
else:
    st.write("Aún no has tirado la moneda.")
