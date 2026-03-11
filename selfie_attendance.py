import streamlit as st
import face_recognition
import pickle
import pandas as pd
from datetime import datetime
import numpy as np
from PIL import Image
import os
import cv2

st.title("📸 Selfie Attendance System")

# Load face encodings
with open("encodings/faces.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

uploaded_file = st.file_uploader("Upload Class Selfie", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np, face_locations)

    present_students = []

    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):

        face_distances = face_recognition.face_distance(known_encodings, encoding)
        best_match_index = face_distances.argmin()

        name = "Unknown"

        if face_distances[best_match_index] < 0.45:
            name = known_names[best_match_index]

            if name not in present_students:
                present_students.append(name)

        # Draw rectangle on face
        cv2.rectangle(image_np, (left, top), (right, bottom), (0,255,0), 2)

        # Name label
        cv2.rectangle(image_np, (left, bottom-30), (right, bottom), (0,255,0), cv2.FILLED)
        cv2.putText(image_np, name, (left+6, bottom-6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)

    st.image(image_np, caption="Detected Faces")

    if len(present_students) > 0:

        st.success("Attendance Marked Successfully")

        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")

        if not os.path.exists("attendance.csv"):
            df = pd.DataFrame(columns=["Name","Date","Time"])
            df.to_csv("attendance.csv", index=False)

        existing_df = pd.read_csv("attendance.csv")

        for student in present_students:

            # duplicate block
            if not ((existing_df["Name"] == student) & (existing_df["Date"] == date)).any():

                df = pd.DataFrame([[student, date, time]], columns=["Name","Date","Time"])
                df.to_csv("attendance.csv", mode="a", header=False, index=False)

        st.subheader("✅ Present Students")
        st.write(present_students)

        # Absent list
        all_students = list(set(known_names))
        absent_students = [s for s in all_students if s not in present_students]

        st.subheader("❌ Absent Students")
        st.write(absent_students)

    else:
        st.warning("No registered student detected")