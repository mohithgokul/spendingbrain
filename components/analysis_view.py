import streamlit as st
from utils.detection import detect_overspending
from utils.ai_insights import generate_insights

def show_analysis():
    st.header("🚨 Smart Spending Analysis")

    df = st.session_state.df

    if df is None:
        st.warning("Upload data first")
        return

    # 📊 Summary
    st.subheader("📊 Spending Summary")
    st.write(df.groupby("Category")["Amount"].sum())

    # 🚨 Rule-based alerts
    st.subheader("🚨 Alerts")
    alerts = detect_overspending(df)

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("✅ No major issues detected")

    # 🤖 AI Insights
    st.subheader("🤖 AI Financial Advice")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing your spending..."):
            insights = generate_insights(df)
            st.write(insights)