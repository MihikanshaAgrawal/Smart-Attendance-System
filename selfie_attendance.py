import streamlit as st
import face_recognition
import pickle
import pandas as pd
from datetime import datetime
import numpy as np
from PIL import Image
import os

def show():

    st.subheader("📸 Selfie Attendance")

    with open("encodings/faces.pkl","rb") as f:
        data=pickle.load(f)

    known_encodings=data["encodings"]
    known_names=data["names"]

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        uploaded_file=st.file_uploader(
        "Upload Class Selfie",
        type=["jpg","jpeg","png"]
        )

        if uploaded_file is not None:

            image=Image.open(uploaded_file)
            image_np=np.array(image)

            st.image(image,caption="Uploaded Selfie")

            face_locations=face_recognition.face_locations(image_np)
            face_encodings=face_recognition.face_encodings(image_np,face_locations)

            present_students=[]

            for encoding in face_encodings:

                face_distances=face_recognition.face_distance(
                known_encodings,encoding)

                best_match_index=face_distances.argmin()

                if face_distances[best_match_index] <0.45:

                    name=known_names[best_match_index]

                    if name not in present_students:
                        present_students.append(name)

            if len(present_students)>0:

                st.success("✅ Attendance Marked")

                date=datetime.now().strftime("%Y-%m-%d")
                time=datetime.now().strftime("%H:%M:%S")

                filename=f"attendance_{date}.csv"

                if not os.path.exists(filename):
                    df=pd.DataFrame(columns=["Name","Time"])
                    df.to_csv(filename,index=False)

                existing_df=pd.read_csv(filename)

                for student in present_students:

                    if student not in existing_df["Name"].values:

                        df=pd.DataFrame(
                        [[student,time]],
                        columns=["Name","Time"]
                        )

                        df.to_csv(
                        filename,
                        mode="a",
                        header=False,
                        index=False
                        )

                st.write("### Present Students")
                st.success(present_students)

            else:
                st.warning("No registered student detected")