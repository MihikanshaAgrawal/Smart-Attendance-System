import streamlit as st
import pandas as pd
from datetime import datetime
import os

def show():

    st.subheader("📊 Today Attendance Dashboard")

    date=datetime.now().strftime("%Y-%m-%d")
    filename=f"attendance_{date}.csv"

    if not os.path.exists(filename):

        st.warning("⚠ No attendance taken today")

    else:

        df=pd.read_csv(filename)

        total_students=len(df)

        col1,col2=st.columns(2)

        with col1:
            st.metric("Total Present",total_students)

        with col2:
            st.metric("Date",date)

        st.write("### Attendance Table")
        st.dataframe(df,use_container_width=True)

        st.write("### Attendance Count")

        attendance_count=df["Name"].value_counts().reset_index()
        attendance_count.columns=["Student Name","Attendance"]

        st.bar_chart(
        attendance_count.set_index("Student Name")
        )