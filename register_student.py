import streamlit as st
import os
import mihikansha 

DATASET_DIR = "dataset"

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

st.title("Student Registration")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")

uploaded_file = st.file_uploader("Upload Student Photo", type=["jpg", "jpeg", "png"])

if st.button("Register Student"):
    if name and roll and uploaded_file:
        filename = f"{name}_{roll}.jpg"
        path = os.path.join(DATASET_DIR, filename)

        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Student {name} registered successfully!")
    else:
        st.error("Please fill all details and upload photo.")