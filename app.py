import streamlit as st

st.title("Clasificador de temperatura")

temperatura = st.number_input(
    "Introduce la temperatura en °C:",
    value=20
)

if temperatura < 10:
    st.write("Hace frío.")
elif temperatura < 25:
    st.write("La temperatura es agradable.")
else:
    st.write("Hace calor.")
