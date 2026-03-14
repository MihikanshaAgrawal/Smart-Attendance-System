import streamlit as st
import pandas as pd

def login():

    st.title("👨‍🏫 Teacher Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        teachers = pd.read_csv("teachers.csv")

        teachers["Username"] = teachers["Username"].astype(str)
        teachers["Password"] = teachers["Password"].astype(str)

        user = teachers[
            (teachers["Username"] == username.strip()) &
            (teachers["Password"] == password.strip())
        ]

        if len(user) > 0:

            st.session_state["logged_in"] = True
            st.session_state["teacher_name"] = user.iloc[0]["Name"]
            st.session_state["subject"] = user.iloc[0]["Subject"]

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Username or Password")