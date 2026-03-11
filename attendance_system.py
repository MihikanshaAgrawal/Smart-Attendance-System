import face_recognition
import cv2
import pickle
import pandas as pd
from datetime import datetime
import os

# load encodings
with open("encodings/faces.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# create attendance file if not exists
if not os.path.exists("attendance.csv"):
    df = pd.DataFrame(columns=["Name","Date","Time"])
    df.to_csv("attendance.csv", index=False)

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Camera started...")

while True:

    ret, frame = video.read()

    if not ret:
        print("Camera error")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for encoding in face_encodings:

        matches = face_recognition.compare_faces(known_encodings, encoding)

        if True in matches:

            index = matches.index(True)
            name = known_names[index]

            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")

            df = pd.DataFrame([[name, date, time]], columns=["Name","Date","Time"])

            df.to_csv("attendance.csv", mode="a", header=False, index=False)

            print(name, "Attendance Marked")

            video.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()