# Warehouse Locator (tuples)
# A logistics team stores warehouse locations as (city, latitude, longitude) tuples

warehouses = [
    ("Delhi", 28.61, 77.21),
    ("Mumbai", 19.08, 72.88),
    ("Chennai", 13.08, 80.27),
    ("Kolkata", 22.57, 88.36),
    ("Jaipur", 26.91, 75.79)
]

cities = []
lat_1 = []
new_warehouses = []
data = ()

for city, lat, long in warehouses:
    cities.append(city)
    lat_1.append(lat)


for city, lat in zip(cities,lat_1):
    if lat == max(lat_1):
        print(f"Northanmost : {city} , {lat}")
        data += (city,lat)
        new_warehouses.append(data)


    if lat == min(lat_1):
        print(f"Southanmost : {city} , {lat}")
        data += (city,lat)
        new_warehouses.append(data)

print(new_warehouses)