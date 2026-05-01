# Read input as integer
num = int(input())

reverse = 0

# Reverse using while loop
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)
