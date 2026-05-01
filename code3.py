from datetime import date

from datetime import date

# write your code here...

# Read input dates
d1 = input().strip()
d2 = input().strip()

# Split the dates into year, month, day
y1, m1, day1 = map(int, d1.split("-"))
y2, m2, day2 = map(int, d2.split("-"))

# Create date objects
date1 = date(y1, m1, day1)
date2 = date(y2, m2, day2)

# Calculate difference
difference = date2 - date1

# Print number of days
print(difference.days)
