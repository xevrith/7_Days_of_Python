# Festival Discount Engine
# An e-commerce site runs a festival sale with stacked discount rules.

tests = [("Gold", 12000, True), ("Silver", 6000, False), ("None", 3000, True)]

gold_discount = 0.15
silver_discount = 0.10
festive_discount = 0.3
above_extra = 0.5
is_festival = True

for customers in tests:
    if "Gold" in customers:
        if customers[-1] == is_festival:
            total_discount = 0
            cal_discount = customers[1] * gold_discount
            total_discount += gold_discount

            if customers[10] >= 5000:
                cal_discount2 = customers[1] * above_extra
                total_discount += above_extra

                