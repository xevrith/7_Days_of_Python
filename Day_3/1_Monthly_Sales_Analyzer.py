# Monthly Sales Analyzer
# Head office wants a quick analysis of last year's monthly sales (in thousands of rupees).

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [420, 380, 450, 510, 480, 530, 610, 590, 560, 640, 720, 810]


for month, sale in zip(months,sales):
    if sale == min(sales):
        print(f"Worst Month : {month}")

    if sale == max(sales):
        print(f"Best Month : {month}")

print(f"Total Sales : {sum(sales)}")
print(f"Average Sales : {round(sum(sales) / len(sales),1)}")