import streamlit as st
import os
import re

def show():

    st.subheader("👨‍🎓 Register New Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")

    uploaded_file = st.file_uploader(
        "Upload Student Photo",
        type=["jpg","jpeg","png"]
    )

    if st.button("Register Student"):

        if name and roll and uploaded_file:

            # create dataset folder
            if not os.path.exists("dataset"):
                os.makedirs("dataset")

            # remove invalid characters from roll number
            clean_roll = re.sub(r'[^a-zA-Z0-9]', '_', roll)

            filename = f"{name}_{clean_roll}.jpg"
            path = os.path.join("dataset", filename)

            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("✅ Student Registered Successfully")

        else:
            st.error("Please fill all details")