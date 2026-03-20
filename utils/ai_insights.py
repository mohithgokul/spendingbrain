import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_insights(df):
    category_sum = df.groupby("Category")["Amount"].sum().to_dict()
    total = df["Amount"].sum()

    prompt = f"""
    You are a smart financial advisor.

    Analyze the user's spending:

    Total Spending: ₹{total}
    Category Breakdown: {category_sum}

    Give:
    1. Key observations
    2. Overspending warnings
    3. Practical saving tips

    Keep it short, clear, and helpful.
    """

    response = model.generate_content(prompt)

    return response.text

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