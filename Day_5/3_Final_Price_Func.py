# Final Price Function
# Write calculate_final_price(price, discount_pct=10, gst_pct=18)

def calculate_final_price(price, discount_pct=10, gst_pct=18):
    get_discount = price * (discount_pct / 100)
    get_price = price - get_discount
    get_gst = get_price * (gst_pct / 100)
    final_price = get_price - get_gst
    print(f"Final Price : {final_price}")

calculate_final_price(1000)