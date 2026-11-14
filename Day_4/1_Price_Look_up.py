# Price Lookup & Cart Bill
# Billing software looks up prices by product name.

prices = {"rice": 62, "atta": 48, "sugar": 45, "milk": 30}
cart = {"rice": 3, "milk": 4}

print(f"Sugar Price : {prices['sugar']}")

search = input("Enter name : ")
print(f"{search} : {prices.get(search)}")

prices["Oil"] = 165
print(prices)

prices["sugar"] = 47
print(f"Updated Sugar Price : {prices['sugar']}")

prices.pop("atta")
print(prices.get("atta"))

print("milk" in prices)

print(f"Rice : {prices['rice']} x {cart['rice']} = {prices['rice'] * cart['rice']}")
print(f"Milk : {prices['milk']} x {cart['milk']} = {prices['milk'] * cart['milk']}")
print(f"Total Bill {(prices['milk'] * cart['milk']) + (prices['rice'] * cart['rice'])}")