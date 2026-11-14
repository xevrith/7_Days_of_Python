# Order Status Tracker
# Operations tracks every order by status.

orders = {
    "O1001": "Delivered",
    "O1002": "Shipped",
    "O1003": "Delayed",
    "O1004": "Delivered",
    "O1005": "Delayed",
    "O1006": "Cancelled"
}

status_count = {}
status2 = []
for status in orders.values():
    status2.append(status)

for status in status2:
    status_count[status] = status2.count(status)

print(status_count)

orders["O1003"] = "Shipped"
orders["O1007"] = "Shipped"
print(orders)

cancel_orders = []

for order,status in orders.items():
    if status == "Cancelled":
        cancel_orders.append(order)


for order in cancel_orders:
    if order in orders:
        orders.pop(order)

print(orders)