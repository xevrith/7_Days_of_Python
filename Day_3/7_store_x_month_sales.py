# Store x Month Sales Matrix
# Four stores, six months. Analyse the table without any library
import numpy as np

sales = [
 [120, 135, 150, 160, 155, 170], # Store A (Jan..Jun)
 [200, 190, 210, 220, 230, 240], # Store B
 [ 90, 100, 95, 110, 105, 130], # Store C
 [150, 160, 170, 165, 180, 175], # Store D
]

new_list = np.array(sales)


print(f"Total Sum : {np.sum(new_list)}")
print(f"Each Store Total : {np.sum(new_list,axis=1)}")
print(f"Month Sales : {np.sum(new_list,axis=0)}")



