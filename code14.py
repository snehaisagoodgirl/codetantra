import numpy as np

# Input rows and columns
r, c = map(int, input().split())

# Handle empty case
if r == 0 and c == 0:
    arr = np.array([]).reshape(0, 0)
else:
    elements = []
    
    # Take input row by row
    for _ in range(r):
        row = list(map(int, input().split()))
        elements.extend(row)
    
    # Create and reshape array
    arr = np.array(elements).reshape(r, c)

# Output
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
