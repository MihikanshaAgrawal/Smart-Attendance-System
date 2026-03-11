import streamlit as st
import os

DATASET_DIR = "dataset"

# dataset folder automatically create
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

def show():

    st.header("Student Registration")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")

    uploaded_file = st.file_uploader(
        "Upload Student Photo",
        type=["jpg","jpeg","png"]
    )

    if st.button("Register Student"):

        if name and roll and uploaded_file:

            # remove invalid characters from roll
            roll = roll.replace("/", "_")
            roll = roll.replace("\\", "_")
            roll = roll.replace(" ", "_")

            filename = f"{name}_{roll}.jpg"

            path = os.path.join(DATASET_DIR, filename)

            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("Student Registered Successfully ✅")

        else:
            st.error("Please fill all details and upload photo")