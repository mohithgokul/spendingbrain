import streamlit as st

def show_goals():
    st.header("🎯 Financial Goal Planning")

    df = st.session_state.df

    if df is None:
        st.warning("Upload data first")
        return

    # 🎯 User input
    goal = st.number_input("Enter your goal amount (₹)", min_value=0)
    months = st.slider("Time to achieve goal (months)", 1, 24)

    if goal > 0:
        monthly_required = goal / months

        st.subheader("📊 Goal Breakdown")
        st.info(f"You need to save ₹{monthly_required:.0f} per month")

        # 💸 Current spending
        total_spend = df["Amount"].sum()
        monthly_spend = total_spend  # assuming current data is monthly

        st.subheader("📉 Your Current Spending")
        st.write(f"Monthly spending: ₹{monthly_spend:.0f}")

        # 🚨 Compare
        if monthly_spend > monthly_required:
            st.error("⚠️ You are spending too much to reach your goal!")
            st.write(f"Reduce spending to ₹{monthly_spend - monthly_required:.0f}")
        else:
            st.success("✅ You are on track to reach your goal!")