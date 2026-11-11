# Review Sentiment Counter
# Customer reviews must be tagged POSITIVE, NEGATIVE or NEUTRAL.

reviews = ["Great product, fast delivery!", "Terrible quality. Broke in 2 days.","Good value for money", "Not good, very slow delivery", "Excellent!! Loved it", "Worst purchase ever"]

positive_words = ["Great", "fast", "Good", "value", "Excellent", "Loved"]
negative_words = ["Terrible", "Broke", "slow", "Worst"]
clean_review = []
customer_review = []

positive = 0
negative = 0


for review in reviews:
    clean_review.append(review.replace(",","").replace("!","").replace(".",""))

for review in clean_review:
    for word in positive_words:
        if positive_words in review.split(" "):
            positive += 1
            if positive >= 1:
                customer_review.append("POS")

print(customer_review)



