import streamlit as st
import register_student
import selfie_attendance
import dashboard

st.set_page_config(
    page_title="Smart Attendance System",
    page_icon="🎓",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#1f4037,#99f2c8);
}

h1{
text-align:center;
color:white;
}

.block-container{
padding-top:2rem;
}

.card{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0 8px 20px rgba(0,0,0,0.2);
}

.sidebar .sidebar-content{
background:#1c2833;
}

</style>
""",unsafe_allow_html=True)

st.title("🎓 Smart Attendance System")

menu = ["Register Student","Selfie Attendance","Dashboard"]

choice = st.sidebar.selectbox("Menu",menu)

if choice=="Register Student":
    register_student.show()

elif choice=="Selfie Attendance":
    selfie_attendance.show()

elif choice=="Dashboard":
    dashboard.show()