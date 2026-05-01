import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)


daily_transcriptions = df.groupby('Date')['Product'].apply(list)
pair_counts= Counter()

# Output the most frequent product pairs
for products in daily_transcriptions:
	products = sorted(products)
	pairs = list(combinations(products, 2))
	pair_counts.update(pairs)

if pair_counts:
	max_count = max(pair_counts.values())
	for pair,count in pair_counts.items():
		if count == max_count:
			print(f"{pair[0]} and {pair[1]}: {count} times")
else:
	print("No product pair found. ")
