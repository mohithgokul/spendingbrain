import streamlit as st

from components.upload import show_upload

st.set_page_config(page_title="Spending Brain", layout="wide")

st.title("🧠 Spending Brain")
st.write("AI-Based Personal Finance Coach")

# Sidebar
menu = st.sidebar.radio("Navigation", [
    "Upload Data",
    "Dashboard",
    "Analysis",
    "AI Insights",
    "Goals"
])

# Session state
if "df" not in st.session_state:
    st.session_state.df = None

# Routing
if menu == "Upload Data":
    show_upload()

elif menu == "Dashboard":
    st.write("Dashboard coming soon...")

elif menu == "Analysis":
    st.write("Analysis coming soon...")

elif menu == "AI Insights":
    st.write("AI insights coming soon...")

elif menu == "Goals":
    st.write("Goals coming soon...")