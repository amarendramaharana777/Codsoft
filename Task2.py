def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter the number corresponding to the operation : "))

        
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

       
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

       
        if choice == 1:
            result = num1 + num2
            operation = "+"
        elif choice == 2:
            result = num1 - num2
            operation = "-"
        elif choice == 3:
            result = num1 * num2
            operation = "*"
        elif choice == 4:
            if num2 == 0: 
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "/"

       
        print(f"The result of {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers and a valid operation choice.")

if __name__ == "__main__":
    calculator()
