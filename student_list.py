import streamlit as st
import os
import pandas as pd

def show():

    st.header("👨‍🎓 Student List")

    if not os.path.exists("dataset"):
        st.warning("No students registered yet")
        return

    files = os.listdir("dataset")

    if len(files) == 0:
        st.warning("No students found")
        return

    students = []

    for file in files:

        name_roll = os.path.splitext(file)[0]

        if "_" in name_roll:
            name, roll = name_roll.split("_",1)
        else:
            name = name_roll
            roll = "N/A"

        students.append({
            "Name": name,
            "Roll": roll,
            "File": file
        })

    df = pd.DataFrame(students)

    # search
    search = st.text_input("🔍 Search Student")

    if search:
        df = df[df["Name"].str.contains(search, case=False)]

    for index,row in df.iterrows():

        col1,col2,col3,col4 = st.columns([1,3,2,1])

        image_path = os.path.join("dataset",row["File"])

        with col1:
            st.image(image_path,width=80)

        with col2:
            st.write(f"**{row['Name']}**")

        with col3:
            st.write(f"Roll: {row['Roll']}")

        with col4:

            if st.button("Delete", key=row["File"]):

                os.remove(image_path)

                st.success("Student Deleted")

                st.rerun()