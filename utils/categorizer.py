CATEGORY_KEYWORDS = {

    "Food": [
        "zomato", "swiggy", "dominos", "pizza hut", "kfc", "burger king",
        "subway", "restaurant", "cafe", "dine", "food", "eat", "biryani",
        "starbucks", "coffee", "tea", "bakery", "tiffin", "mess", "canteen", "hello idle", "slice of life", "paradise"
    ],

    "Transport": [
        "uber", "ola", "rapido", "bus", "train", "metro",
        "fuel", "petrol", "diesel", "auto", "cab", "irctc",
        "flight", "air", "taxi", "parking", "toll"
    ],

    "Shopping": [
        "amazon", "flipkart", "myntra", "ajio", "meesho",
        "shopping", "store", "purchase", "mall", "fashion",
        "clothes", "electronics", "order", "delivery"
    ],

    "Subscription": [
        "netflix", "amazon prime", "prime", "hotstar", "disney",
        "zee5", "sony liv", "spotify", "youtube premium",
        "apple music", "subscription", "google one",
        "icloud", "microsoft 365", "adobe", "aha", "alt balaji", "voot"
    ],

    "Bills": [
        "electricity", "water bill", "gas bill", "internet",
        "wifi", "broadband", "recharge", "mobile bill",
        "postpaid", "prepaid", "dth", "airtel", "jio", "vi",
        "bsnl", "utility"
    ],

    "Health": [
        "hospital", "pharmacy", "medicine", "doctor",
        "clinic", "apollo", "health", "medical",
        "lab", "diagnostic", "test", "scan"
    ],

    "Education": [
        "course", "udemy", "coursera", "college",
        "school", "fees", "tuition", "exam",
        "training", "class", "learning"
    ],

    "Entertainment": [
        "movie", "bookmyshow", "game", "concert",
        "event", "ticket", "fun", "show",
        "theatre", "cinema", "net cafe"
    ],

    "Finance": [
        "loan", "emi", "interest", "bank", "credit card",
        "debit", "payment", "transfer", "upi",
        "gpay", "phonepe", "paytm", "famapay", "supermoney"
    ],

    "Travel": [
        "hotel", "oyo", "booking", "airbnb",
        "trip", "travel", "makemytrip",
        "goibibo", "stay", "resort"
    ],

    "Others": []
}


def categorize(description):
    desc = str(description).lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in desc:
                return category

    return "Others"