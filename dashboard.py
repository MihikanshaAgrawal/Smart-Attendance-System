py -3.10 -m pip listimport streamlit as st
import pandas as pd
import os

st.title("📊 Smart Attendance Dashboard")

if not os.path.exists("attendance.csv"):
    st.warning("No attendance data found")

else:

    df = pd.read_csv("attendance.csv")

    st.subheader("Attendance Table")
    st.dataframe(df)

    st.subheader("Student Attendance Count")

    # count attendance per student
    count = df["Name"].value_counts().reset_index()

    count.columns = ["Student Name", "Attendance Count"]

    # show numbers clearly
    st.table(count)

    st.subheader("Attendance Graph")

    st.bar_chart(count.set_index("Student Name"))