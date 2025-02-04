# calculates the maximum number of steps required for binary search on a sorted list of 128 names

import math

n = 128

# Calculate the maximum number of steps using log2
max_steps = math.log2(n)

# math.ceil to round up
max_steps = math.ceil(max_steps)

print(f"The maximum number of steps required to search through a list of {n} names is: {max_steps}")