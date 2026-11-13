# Duplicate Order Remover
# The order feed sometimes sends the same order ID more than once.

orders = ["ORD101", "ORD102", "ORD101", "ORD103", "ORD102", "ORD104", "ORD101"]
unique_order = []
duplicate_orders = []

for order in orders:
    if orders.count(order) > 1:
        duplicate_orders.append(order)

    else:
        unique_order.append(order)

print(f"Unique Orders : {unique_order}")
print(f"Duplicate Orders : {duplicate_orders}")
