import google.generativeai as genai

genai.configure(api_key="API_KEY")

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

