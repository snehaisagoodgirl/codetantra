# write your code here...

num = int(input())

# Check if number is within valid range
if 1 <= num <= 999:
    digits = len(str(num))
    
    if digits == 1:
        # Single digit → square
        print(num ** 2)
        
    elif digits == 2:
        # Two digits → square root
        print(f"{num ** 0.5:.2f}")
        
    elif digits == 3:
        # Three digits → cube root
        print(f"{num ** (1/3):.2f}")
else:
    print("Invalid")
