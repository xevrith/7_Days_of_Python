# Data Quality Scanner
# Before analysis you must check the Age column of a customer table

ages = [25, 31, -4, 47, 150, 29, 0, 38, 62, 17, 999, 41]
valid_age = []
invalid_age = []

for age in ages:
    if age >= 18 and age <= 100:
        valid_age.append(age)
    else:
        invalid_age.append(age)

print(f"Valid Age : {len(valid_age)}")
print(f"Invalid Age : {len(invalid_age)}")
print(f"Average : {sum(valid_age)/len(valid_age)}")
print(f"Yongest : {min(valid_age)}")
print(f"oldest : {max(valid_age)}")