# Category Counter
# Which product categories sell most often?

purchases = [
    "Grocery", "Dairy", "Grocery", "Personal Care",
    "Dairy", "Grocery", "Household", "Dairy",
    "Grocery", "Personal Care"
]

category = {}

for item in purchases:
    category[item] = purchases.count(item)

sorted_category = dict(sorted(category.items(),key=lambda item: item[1]))
total = sum(sorted_category.values())

percentage = {k: (v / total) * 100 for k, v in sorted_category.items()}
print(percentage)