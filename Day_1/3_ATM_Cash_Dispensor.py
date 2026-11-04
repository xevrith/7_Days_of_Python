# ATM Cash Dispenser
# An ATM must hand out the minimum number of notes.

try:
    amount = int(input("Enter the withdraw amount : "))

    if amount >= 100 and amount <= 20000:
        if amount % 100 == 0:
           largest_times = amount // 2000
           largest = amount % 2000
            
           second_times = largest // 500
           second_largest = largest % 500

           third_times = second_largest // 200
           third_largest = second_largest % 200

           if third_largest >= 100:
               smallest_times = third_largest // 100
               smallest = third_largest % 100
               print(f"{amount} -> 2000 x {largest_times}, 500 x {second_times}, 200 x {third_times}, 100 x {smallest_times}")

           else:
               print(f"{amount} -> 2000 x {largest_times}, 500 x {second_times}, 200 x {third_times}")

    else:
        print(f"Check your amount again, It must be Between 100 To 20000")
           
except ValueError:
    print(f"Invalid Value")
