import streamlit as st
import login
import register_student
import selfie_attendance
import dashboard
import student_list
# login state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# LOGIN PAGE
if not st.session_state["logged_in"]:
    login.login()

else:

    st.sidebar.success(
        f"Welcome {st.session_state['teacher_name']} ({st.session_state['subject']})"
    )

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    menu = ["Dashboard","Register Student","Student List","Selfie Attendance"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Dashboard":
        dashboard.show()

    elif choice == "Register Student":
        register_student.show()

    elif choice == "Selfie Attendance":
        selfie_attendance.show()
    
    elif choice == "Student List":
        student_list.show()