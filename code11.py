# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# DictOperations.py

# Initial dictionary with 10 records
d = {
    1: 'Amit', 2: 'Riya', 3: 'Kiran', 4: 'Neha', 5: 'Arjun',
    6: 'Pooja', 7: 'Rahul', 8: 'Sneha', 9: 'Vikram', 10: 'Anjali'
}

# Display original dictionary
print("Original Dictionary:", d)

# Insertion
key = int(input())
value = input()
d[key] = value
print("After Insertion:", d)

# Update
key = int(input())
value = input()
if key in d:
    d[key] = value
print("After Update:", d)

# Deletion
key = int(input())
if key in d:
    d.pop(key)
print("After Deletion:", d)

# Traversal
print("Traversing Dictionary:")
for k, v in d.items():
    print(k, ":", v)

