# Top Customers with Ties
# Marketing wants to reward the top 3 spenders - but a tie at 3rd place should include everyone tied

spend = [
    ("Asha", 15400),
    ("Ravi", 9800),
    ("Meena", 22150),
    ("Karan", 15400),
    ("Divya", 4300),
    ("Imran", 18200)
]

customers = []
amount_spend = []

sorted_spend = list(sorted(spend,key=lambda x: x[-1],reverse=True))
print(sorted_spend)

for customer, amount in sorted_spend:
    customers.append(customer)
    amount_spend.append(amount)

print(f"Top 4 Spendings")

count = 0

for customer, amount in sorted_spend:
    if count < 4:
        print(f"{customer} : {amount}")

    count += 1

total = 0

print(f"Average Spending : {round(sum(amount_spend) / len(amount_spend),2)}")

