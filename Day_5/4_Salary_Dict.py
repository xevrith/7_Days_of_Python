# Salary Dict Comprehensions
# HR wants quick transformations of a salary dictionary.

salaries = {"Asha":42000, "Ravi":78000, "Meena":55000, "Karan":91000, "Divya":47000}

salaries_hike = {k:v + (v * 0.08 / 100) for k,v in salaries.items()}
print(salaries_hike)

rank = {k: ("A" if v > 80000 else "B" if v > 50000 else "C") for k,v in salaries_hike.items()}
print(rank)