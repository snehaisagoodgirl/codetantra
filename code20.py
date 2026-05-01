import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# 1. Find indices where value matches in array1
indices = np.where(array1 == search_value)[0]

# 2. Count occurrences in array1
count = np.count_nonzero(array1 == count_value)

# 3. Broadcasting addition
broadcasted_array = array1 + broadcast_value

# 4. Sort the array
sorted_array = np.sort(array1)

# Output
print(indices)
print(count)
print(broadcasted_array)
print(sorted_array)
