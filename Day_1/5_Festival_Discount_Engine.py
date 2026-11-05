# Festival Discount Engine
# An e-commerce site runs a festival sale with stacked discount rules.

tests = [("Gold", 12000, True), ("Silver", 6000, False), ("None", 3000, True)]

gold_discount = 0.15
silver_discount = 0.10
festive_discount = 0.03
above_extra = 0.05
is_festival = True

for customers in tests:
    membership = customers[0]
    festival = customers[-1]
    amount = customers[1]

    total_discount = 0

    if membership == "Gold":
        total_discount += gold_discount

        if amount >= 5000:
            total_discount += above_extra

    if membership == "Silver":
        total_discount += silver_discount

        if amount >= 5000:
            total_discount += above_extra

    if festival == is_festival:
        total_discount += festive_discount

    if total_discount > 0.25:
        total_discount == 0.25

    if amount * total_discount > 2000:
        discount_amount = 2000

    final_amount = amount - discount_amount

    print(f"{membership} Final Amount: {final_amount:.2f}")
    



                          
                

                