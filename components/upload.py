import streamlit as st
import pandas as pd
from utils.categorizer import categorize

def show_upload():
    st.header("📂 Upload Your Transactions")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        df.columns = ["Date", "Description", "Amount"]
        df["Category"] = df["Description"].apply(categorize)

        st.session_state.df = df

        st.success("✅ Data uploaded successfully!")
        st.dataframe(df)
    if st.session_state.df is None:
        st.info("👆 Please upload a file to get started")
        