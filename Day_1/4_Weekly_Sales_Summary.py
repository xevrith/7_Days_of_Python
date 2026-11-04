# Weekly Sales Summary
# The shop owner sends 7 daily sales figures every Sunday night

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [12500, 9800, 15200, 11000, 18700, 21000, 7600]

print(f"Total : {sum(sales)}")
print(f"Average : {round(sum(sales) / len(sales),2)}")

for day,sale in zip(days,sales):
    if sale == max(sales):
        print(f"Best {day} {sale}")

    if sale == min(sales):
        print(f"Worset {day} {sale}")

count = 0

for sale in sales:
    if sale > (sum(sales)/len(sales)):
        count += 1

print(f"{count} Days Above Average")
