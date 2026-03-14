import streamlit as st
import os
import re
import face_recognition
import pickle

def show():

    st.header("Register Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")

    uploaded_file = st.file_uploader(
        "Upload Student Photo",
        type=["jpg","jpeg","png"]
    )

    if st.button("Register Student"):

        if name and roll and uploaded_file:

            if not os.path.exists("dataset"):
                os.makedirs("dataset")

            clean_roll = re.sub(r'[^a-zA-Z0-9]', '_', roll)

            filename = f"{name}_{clean_roll}.jpg"
            path = os.path.join("dataset", filename)

            with open(path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("Student Registered")

            # auto encoding

            known_encodings = []
            known_names = []

            for file in os.listdir("dataset"):

                image = face_recognition.load_image_file(
                    os.path.join("dataset", file)
                )

                enc = face_recognition.face_encodings(image)

                if len(enc) > 0:

                    known_encodings.append(enc[0])
                    known_names.append(os.path.splitext(file)[0])

            data = {
                "encodings": known_encodings,
                "names": known_names
            }

            if not os.path.exists("encodings"):
                os.makedirs("encodings")

            with open("encodings/faces.pkl", "wb") as f:
                pickle.dump(data, f)

            st.success("Encoding Updated")

        else:
            st.error("Fill all fields")