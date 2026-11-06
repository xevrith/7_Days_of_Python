# Savings Goal Calculator
# A fintech app tells users when they will reach a savings goal

target = 500000.00
balance = 50000.00
monthly_deposit = 8000.00
annual_interest = 0.07 / 12
yearly_data = []
month_count = 0
total_deposited = 0
total_interest = 0
year_count = 0

print(f"Starting Balnace : {balance}")
print(f"Monthly Deposite : {monthly_deposit}")
print(f"Annual Interest Rate : 7%")
print(f"{10*"-"} Yearly Summary {10*"-"}")
print()
while balance < target:
    balance += monthly_deposit
    total_deposited +=  monthly_deposit
    monthly_intre = balance * annual_interest
    balance += monthly_intre
    total_interest += monthly_intre
    month_count += 1

    if month_count % 12 == 0:
        yearly_amount = balance     
        yearly_data.append(yearly_amount)
        update_deposite = monthly_deposit * 0.10
        monthly_deposit += update_deposite


for year in yearly_data:
    year_count += 1
    print(f"Year {year_count} Balance Rs.{round(year,2)}")
print()
print(f"{10*"-"} Final Report {10*"-"}")
print(f"Target Amount : {target}")
print(f"Months Needed : {month_count}")
print(f"Total Deposited : {total_deposited}")
print(f"Total Interest Earned : {round(total_interest)}")


    


