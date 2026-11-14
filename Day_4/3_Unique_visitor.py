# Unique Visitors
# The web team logs user IDs for two days.

day1 = ["u1","u2","u3","u2","u4","u1","u5"]
day2 = ["u2","u6","u7","u2","u3","u8"]

different_users = set(day1)
different_users2 = set(day2)

print(f"Different Users : {len(different_users)}")
print(f"Different Users : {len(different_users2)}")
print(f"Total Visitors : {len(different_users.union(different_users2))}")
print(f"Visitors on Both Days : {different_users.intersection(different_users2)}")
# users who visited on Day 2 but did not visit on Day 1.
print(f"Difference : {different_users2.difference(different_users)}")
print(f"Difference : {different_users.difference(different_users2)}")


