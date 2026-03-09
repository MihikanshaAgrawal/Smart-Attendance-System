# pip install opencv-python
# pip install face-recognition
# pip install numpy
# pip install pandas
# pip install streamlit
# streamlit run app.py

import streamlit as st

st.title("Smart Attendance System")

menu = ["Register Student", "Attendance", "Dashboard"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register Student":
    import register_student
elif choice == "Attendance":
    st.write("Attendance module coming soon")
elif choice == "Dashboard":
    st.write("Dashboard coming soon")