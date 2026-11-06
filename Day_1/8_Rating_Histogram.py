# Rating Histogram
# A product page shows how many customers gave 1 to 5 stars. Draw it in the terminal

r5=42
r4=30
r3=12
r2=6
r1=3

total_review = r5 + r4 + r3 + r2 + r1
average_review = round(((5 * r5) + (4 * r4) + (3*r3) + (2*r2) + (1*r1)) / total_review,1)

review = [r5,r4,r3,r2,r1]
star_count = 5
for star in review:
    print(f"{star_count} Star | {(star//2) * "#"}")
    star_count -= 1

print(total_review)
print(average_review)

