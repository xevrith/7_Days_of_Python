# Support Ticket Tagger
# Route support tickets to the right team by keywords.

tickets = ["Refund not received for order #4521 even after 10 days",
 "App crashes when I open the payment page",
 "Delivery delayed, order #7788 still not shipped",
 "Wrong size delivered, need exchange",
 "Payment deducted twice, please refund"]

billing_count = 0
logistics_count = 0
technical_count = 0
returns_count = 0

for word in tickets:
    if "refund" in word.lower() or "payment" in word.lower():
        billing_count += 1

    elif "delivery" in word.lower() or "shipped" in word.lower():
        logistics_count += 1

    elif "crashes"in word.lower() or "crash" in word.lower():
        technical_count += 1

    elif "exchange" in word.lower() or "wrong" in word.lower():
        returns_count += 1

    else:
        continue
    

print(f"Billing : {billing_count}")
print(f"Logistics : {logistics_count}")
print(f"Technical : {technical_count}")
print(f"Returned : {returns_count}")