import face_recognition
import os
import pickle

DATASET_DIR = "dataset"
ENCODING_FILE = "encodings/faces.pkl"

known_encodings = []
known_names = []

for file in os.listdir(DATASET_DIR):

    path = os.path.join(DATASET_DIR, file)

    image = face_recognition.load_image_file(path)

    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:

        encoding = encodings[0]

        name = os.path.splitext(file)[0]

        known_encodings.append(encoding)
        known_names.append(name)

data = {"encodings": known_encodings, "names": known_names}

if not os.path.exists("encodings"):
    os.makedirs("encodings")

with open(ENCODING_FILE, "wb") as f:
    pickle.dump(data, f)

print("Face encodings saved successfully")