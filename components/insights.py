import streamlit as st
from utils.ai_insights import generate_insights
    # 🤖 AI Insights
def ai_insights():
    st.subheader("🤖 AI Financial Advice")
    df = st.session_state.df

    if st.button("Generate AI Insights"):
        with st.spinner("⚡ Generating insights (few seconds)..."):
            insights = generate_insights(df)
            st.write(insights)
    if df is None:
     st.warning("⚠️ Please upload data first")
    return