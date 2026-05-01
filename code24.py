import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# writ"e your code here..
print("First five rows:")
print(data.head())

Average_age= round(data['Age'].mean(),2)
print("Average age:",Average_age)

upto_B= data[data['Grade'] <= "B"]
print("Students with a grade up to B")
print(upto_B)
