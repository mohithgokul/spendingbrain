# 🧠 Spending Brain

> AI-Based Personal Finance Coach built with Streamlit

---

## 🚀 Overview

**Spending Brain** is a smart personal finance app that helps users analyze their spending habits, detect unnecessary expenses, and get AI-powered financial insights.

Upload your transaction data → get instant dashboards → understand your spending → improve your savings 💸

---

## ✨ Features

- 📂 **Upload Transactions**
  - Upload CSV files of your expenses
  - Automatic data processing

- 🏷️ **Smart Categorization**
  - Detects categories like Food, Transport, Subscriptions, etc.

- 📊 **Interactive Dashboard**
  - Total spending, top category
  - Pie chart & bar chart visualization

- 🧠 **AI Financial Insights**
  - Personalized insights using Gemini AI
  - Spending warnings
  - Smart saving tips

- 🚨 **Leak Detection**
  - Identifies unnecessary or high spending areas

- 🎯 **Goals (Coming Soon)**
  - Set and track financial goals

---

## 🛠️ Tech Stack

- **Frontend & Backend:** Streamlit  
- **Data Processing:** Pandas  
- **Visualization:** Matplotlib  
- **AI:** Google Gemini API  
- **Version Control:** Git & GitHub  

---
## 📂 Project Structure

spendingbrain/

│

├── components/

│ ├── upload.py

│ ├── dashboard.py

│ ├── analysis_view.py

│ ├── insights.py

│ └── goals.py

│

├── utils/

│ ├── categorizer.py

│ ├── detection.py

│ ├── analysis.py

│ └── ai_insights.py

│

├── data/

├── app.py

├── requirements.txt

├── .env

└── README.md


---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository

```bash
git clone [https://github.com/mohithgokul/spendingbrain.git]
cd spendingbrain
pip install -r requirements.txt
Create a .env file:
GEMINI_API_KEY=your_api_key_here
streamlit run app.py
```
🌐 Live Demo

👉 https://spendingbrain.streamlit.app


