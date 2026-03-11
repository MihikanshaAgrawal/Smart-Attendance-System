import streamlit as st
import register_student
import numpy

st.title("Smart Attendance System")

menu = ["Register Student"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register Student":
    register_student.show()