def main():
    options = ["Add", "Subtract", "Multiply", "Divide", "Exit"]
    while True:
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit""")
        
        operation = input("\nChoose operation: ").title()
        if operation not in options:
            print("Invalid operation, try again...")
            continue
        if operation == "Exit":
            return
        try:
            num1, num2 = map(int, input("Enter the values: ").split())

        except ValueError:
            print("ENTER VALID ANSWER.")
            continue
# Prevents code from running calculations on missing variables
        opts(operation, num1, num2)

def opts(o, x, y):
        if o == "Add":
            print(f"Result: {x + y}")
        elif o == "Subtract":
            print(f"Result: {x - y}")
        elif o == "Multiply":
            print(f"Result: {x * y}")
        else:    
            try:
                    print(f"Result: {x / y}")
            except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()