nums = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Integer: ")
        try:
            num = int(val)
            nums.append(num)
            print("List after adding:", nums)
        except ValueError:
            print("Invalid input")

    elif choice == '2':
        if len(nums) == 0:
            print("List is empty")
        else:
            val = input("Integer: ")
            try:
                num = int(val)
                if num in nums:
                    nums.remove(num)
                    print("List after removing:", nums)
                else:
                    print("Element not found")
            except ValueError:
                print("Invalid input")

    elif choice == '3':
        if len(nums) == 0:
            print("List is empty")
        else:
            print(nums)

    elif choice == '4':
        break

    else:
        print("Invalid choice")
