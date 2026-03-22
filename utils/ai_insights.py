from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")

def generate_insights(df):
    category_sum = df.groupby("Category")["Amount"].sum().to_dict()
    category_sum = dict(list(category_sum.items())[:5])
    total = df["Amount"].sum()

    prompt = f"""
Analyze this spending:

Total: ₹{total}
Categories: {category_sum}

Give short:
- Key insight
- One warning
- One saving tip
"""
    try:
     response = model.generate_content(prompt)
     return response.text
    except Exception as e:
     return "⚠️ AI is taking too long. Please try again."
