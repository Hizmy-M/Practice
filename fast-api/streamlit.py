import streamlit as st
import requests  # To call FastAPI

st.title("FastAPI + Streamlit Integration")

# User input
name = st.text_input("Enter your name:")

if st.button("Greet"):
    response = requests.get(f"http://127.0.0.1:8000/greet/{name}")
    if response.status_code == 200:
        st.write(response.json()["message"])
        st.write(response.json()["message1"])
    else:
        st.write("Error fetching data from FastAPI.")
