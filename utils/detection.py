def detect_overspending(df):
    alerts = []

    total = df["Amount"].sum()
    category_sum = df.groupby("Category")["Amount"].sum()

    # Rules (can expand later)
    limits = {
        "Food": 0.4,        # 40%
        "Shopping": 0.3,
        "Entertainment": 0.25
    }

    for category, limit in limits.items():
        if category in category_sum:
            percent = category_sum[category] / total

            if percent > limit:
                alerts.append(f"⚠️ High spending on {category} ({percent*100:.1f}%)")

    return alerts

def detect_money_leaks(df):
    leaks = []

    # 🔁 Recurring transactions (same description repeated)
    recurring = df["Description"].value_counts()
    recurring = recurring[recurring > 2]

    if not recurring.empty:
        for desc, count in recurring.items():
            leaks.append(f"🔁 '{desc}' repeated {count} times (possible subscription)")
 
    # 🪙 Frequent small expenses
    small_expenses = df[df["Amount"] < 300]
    freq_small = small_expenses["Description"].value_counts()
    freq_small = freq_small[freq_small > 3]

    if not freq_small.empty:
        for desc, count in freq_small.items():
            leaks.append(f"🪙 Frequent small expense: '{desc}' ({count} times)")

    return leaks