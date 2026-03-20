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