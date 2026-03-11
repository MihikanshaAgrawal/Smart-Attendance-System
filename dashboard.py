py -3.10 -m pip listimport streamlit as st
import pandas as pd

st.title("Attendance Dashboard")

df = pd.read_csv("attendance.csv")

st.dataframe(df)