def cal():
    print("Simple Calculator")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        resultt = n1 + n2
        print("The result of addition is: ",resultt)
    elif choice == '2':
        resultt = n1 - n2
        print("The result of subtraction is:" , resultt)
    elif choice == '3':
        resultt = n1 * n2
        print("The result of multiplication is:" , resultt)
    elif choice == '4':
        if n2 != 0:
            resultt = n1 / n2
            print("The result of division is:" , resultt)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")


cal()

