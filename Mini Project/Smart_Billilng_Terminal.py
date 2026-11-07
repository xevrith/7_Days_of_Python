# Smart Billing Terminal for a Grocery Store
# Suggested repo name: day01-smart-billing-terminal
# Case study: A neighbourhood grocery shop still writes bills by hand and makes arithmetic mistakes. Build a
# terminal-based billing program the cashier can run all day.

products = {
    1: ["Rice", 62],
    2: ["Wheat", 48],
    3: ["Sugar", 45],
    4: ["Milk", 30],
    5: ["Cooking Oil", 165],
    6: ["Tea", 110]
}

cart = {}

while True:
    try:
        item_number = int(input("Enter Item Number : "))
        if item_number in products:
            if item_number not in cart:
                try:
                    quantity = int(input("Enter Quantity : "))
                    cart[item_number] = [products[item_number][0],products[item_number][1]*quantity]
                    print(f"Item Added")
                except ValueError:
                    print("Enter Valied Value")
            else:
                try:
                    quantity = int(input("Enter Quantity : "))
                    cart[item_number][1] * quantity
                    print(f"Item Added")
                except ValueError:
                    print("Enter Valied Value")
        elif item_number == 0:
            print(f"Thanks For Using Our Service")
            break
        else:
            print("Item Not Available")
    except ValueError:
        print("Invalid Value")


subtotal = 0

for price in cart.values():
    subtotal += price[1]


if subtotal > 500:
    discount = 0.05
    discount_price = subtotal * discount
    price_after_discount = subtotal - discount_price
    gst = 0.05
    gst_amount = price_after_discount * gst
    finall_bill = price_after_discount + gst_amount

    for item in cart.values():
        print(f"{item[0]} : {item[1]}")

    print(f"Subtotal : {subtotal}")
    print(f"Discount : {discount_price}")
    print(f"GST : {gst_amount}")
    print(f"Final Amount : {finall_bill}")

elif subtotal > 1000:
    discount = 0.08
    discount_price = subtotal * discount
    price_after_discount = subtotal - discount_price
    gst = 0.05
    gst_amount = price_after_discount * gst
    finall_bill = price_after_discount + gst_amount

    for item in cart.values():
        print(f"{item[0]} : {item[1]}")
    
    print(f"Subtotal : {subtotal}")
    print(f"Discount : {discount_price}")
    print(f"GST : {gst_amount}")
    print(f"Final Amount : {finall_bill}")

else:
    discount = 0
    gst = 0.05
    gst_amount = subtotal * gst
    finall_bill = subtotal + gst_amount

    for item in cart.values():
        print(f"{item[0]} : {item[1]}")
    
    print(f"Subtotal : {subtotal}")
    print(f"Discount : {discount}")
    print(f"GST : {gst_amount}")
    print(f"Final Amount : {finall_bill}")












