# GST Price List
# Add 18% GST to a price list with one comprehension per task.

def new_price(data):
    new_amount = [round(price + (price * 0.18 / 100),1) for price in data]
    return new_amount

def filters(data):
    filter_price = [price for price in data if price > 500]
    return filter_price

def labeled(data):
    labbled_price = ["Premium" if price > 1000 else "Budget" for price in data]
    return labbled_price


prices = [199, 499, 1299, 2499, 89, 649]
price_with_gst = new_price(prices)

print(f"Price after GST : {price_with_gst}")

filter_data = filters(price_with_gst)
print(f"Filter Data : {price_with_gst}")

status = labeled(filter_data)
print(f"Status : {status}")




