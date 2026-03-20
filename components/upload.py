import streamlit as st
import pandas as pd

def show_upload():
    st.header("📂 Upload Your Transactions")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        df.columns = ["Date", "Description", "Amount"]

        st.session_state.df = df

        st.success("✅ Data uploaded successfully!")
        st.dataframe(df)