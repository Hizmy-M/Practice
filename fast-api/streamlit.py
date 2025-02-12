import streamlit as st
import requests

st.title("FastAPI + Streamlit POST Example")

# User input
name = st.text_input("Enter your name:")

if st.button("Send POST Request"):
    if name.strip():
        # Prepare JSON data
        payload = {"name": name}

        # Send POST request
        response = requests.post("http://127.0.0.1:8000/greet/", json=payload)

        # Handle response
        if response.status_code == 200:
            st.write(response.json()["message"])
        else:
            st.write("Error:", response.status_code, response.text)
    else:
        st.write("Please enter a valid name.")
