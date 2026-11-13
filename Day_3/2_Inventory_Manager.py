# Inventory Manager
# A store keeps its product names in one list and changes it throughout the day.

stock = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]

stock.append("headset")
print(stock)
stock.insert(2,"USB hub")
print(stock)

if "Webcam" in stock:
    stock.remove("Webcam")
    print(f"Webcam Removed")
else:
    print(f"Not exists")

stock.pop()
print(stock)

print(sorted(stock,reverse=True))
print(sorted(stock,reverse=False))

backup = stock.copy()
print(backup)

backup.pop()
print(stock)


for index, value in enumerate(stock):
    print(index, value)

    

