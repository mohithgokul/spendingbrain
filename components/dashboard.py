import streamlit as st
import matplotlib.pyplot as plt

def show_dashboard():
    st.header("📊 Financial Dashboard")

    df = st.session_state.df

    if df is None:
        st.warning("⚠️ Please upload data first")
        return

    # 🔢 Metrics
    total = df["Amount"].sum()
    transactions = len(df)
    category_sum = df.groupby("Category")["Amount"].sum()
    top_category = category_sum.idxmax()
    top_value = category_sum.max()


    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Spend", f"₹{total:.0f}")
    col2.metric("📄 Transactions", transactions)
    col3.metric("🏆 Top Category", f"{top_category} (₹{top_value:.0f})")

    # 📊 Group data
    col1, col2 = st.columns(2)

    # 🥧 Pie Chart
    with col1:
        st.subheader("Spending Distribution")
        fig, ax = plt.subplots()
        ax.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%")
        st.pyplot(fig)

    # 📊 Bar Chart
    with col2:
        st.subheader("Spending by Category")
        st.bar_chart(category_sum)
    if df is None:
     st.warning("⚠️ Please upload data first")
    return