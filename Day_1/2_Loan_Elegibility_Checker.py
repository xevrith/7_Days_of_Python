# Loan Eligibility Checker
# A bank officer needs a quick pre-screening tool that explains rejections instead of just saying NO.

try:
    age = int(input("Enter your age : "))
    monthly_income = float(input("Enter your Salary : "))
    credit_score = int(input("Enter your Credit Score : "))

    if 21 <= age <= 58 and monthly_income >= 25000 and credit_score >= 700:
        try:
            existing_emi = int(input("Enter Your Existing Emi : "))
            salary_40 = existing_emi * 0.40

            if salary_40 > monthly_income:
                print(f"Loan Application rejected dur to existing EMI which is more then 40% of the salary")

            else:
                print(f"Loan Approve, Pass All the Criteria")
        except ValueError:
            print("Wrong Value")

    else:
        print(f"Rejected")
except ValueError:
    print("Invalid Input")