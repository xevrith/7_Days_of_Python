# Delivery Time Outliers
# Delivery minutes contain a few extreme delays that distort the average.
import statistics as s
times = [32, 28, 35, 30, 29, 95, 31, 27, 33, 110, 30, 34]
average_time = round(sum(times) / len(times),2)
print(f"Average : {average_time}")
print(f"Median : {s.median(times)}")

for outliers in times:
    if outliers * 1.5 > average_time:
        times.remove(outliers)
        print("Deleted")

average_time = sum(times) / len(times)
print(f"Average : {average_time}")
print(f"Median : {s.median(times)}")

