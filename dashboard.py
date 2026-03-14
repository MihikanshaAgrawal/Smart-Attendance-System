import streamlit as st
import pandas as pd
import os

def show():

    subject = st.session_state["subject"]

    st.title(f"📊 {subject} Attendance Dashboard")

    folder = f"attendance/{subject}"

    if not os.path.exists(folder):

        st.warning("No attendance taken yet")

        return

    files = sorted(os.listdir(folder))

    if len(files) == 0:

        st.warning("No attendance records")

        return

    # student list
    students = []

    for file in os.listdir("dataset"):

        name = os.path.splitext(file)[0]

        students.append(name)

    students = sorted(students)

    table = pd.DataFrame({"Student":students})

    for file in files:

        date = file.replace(".csv","")

        df = pd.read_csv(f"{folder}/{file}")

        present = df["Name"].tolist()

        column = []

        for student in students:

            if student in present:
                column.append("P")
            else:
                column.append("A")

        table[date] = column

    table["Total"] = (table.iloc[:,1:]=="P").sum(axis=1)

    total_days = len(files)

    table["Attendance %"] = (table["Total"]/total_days*100).round(1)

    st.dataframe(table,use_container_width=True)

    st.subheader("📈 Attendance Graph")

    graph = table[["Student","Total"]].set_index("Student")

    st.bar_chart(graph)