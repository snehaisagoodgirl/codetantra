# write your code here

n = int(input().strip())
marks = list(map(int, input().split()))

# Check fail condition
if any(m < 40 for m in marks):
    print("Fail")
else:
    average = sum(marks) / n
    print(f"Aggregate Percentage: {average:.2f}")
    
    if average > 75:
        print("Grade: Distinction")
    elif average >= 60:
        print("Grade: First Division")
    elif average >= 50:
        print("Grade: Second Division")
    else:
        print("Grade: Third Division")
