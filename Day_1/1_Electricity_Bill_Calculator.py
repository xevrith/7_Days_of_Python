# # Electricity Bill Calculator
# A state electricity board charges by slabs. Build the bill generator for the billing counter

try:
    units_consumed = int(input("Enter Units : "))
    fixed_charge = 50
    duty = 0.05

    if units_consumed <= 100:
        units = units_consumed * 5
        calculate_duty = units * duty
        total_bill = units + calculate_duty + fixed_charge
        print(f"{units_consumed} units -> energy charge Rs.{units}, duty Rs.{calculate_duty}, fixed {fixed_charge}, total Rs.{total_bill}")

    elif units_consumed > 100 and units_consumed <= 200:
        units = 100 * 5
        remaining_units = (units_consumed - 100) * 7
        energy_charge = units + remaining_units
        calculate_duty = energy_charge * duty
        total_bill = energy_charge + calculate_duty + fixed_charge
        print(f"{units_consumed} units -> energy charge Rs.{energy_charge}, duty Rs.{calculate_duty}, fixed {fixed_charge}, total Rs.{total_bill}")

    else:
        units = 100 * 5
        remaining_units = (units_consumed - 200) * 10
        energy_charge = units + remaining_units
        calculate_duty = energy_charge * duty
        total_bill = energy_charge + calculate_duty + fixed_charge
        print(f"{units_consumed} units -> energy charge Rs.{energy_charge}, duty Rs.{calculate_duty}, fixed {fixed_charge}, total Rs.{total_bill}")


except ValueError:
    print("Invalid Value")