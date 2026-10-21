import math

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
            numbers = list(map(int, input("Enter the values: ").split()))

        except ValueError:
            print("ENTER VALID ANSWER.")
            continue
# Prevents code from running calculations on missing variables
        if not numbers:
            print("No numbers were entered.")
            continue
        opts(operation, numbers)

def opts(o, nums):
        if o == "Add":
            print(f"Result: {sum(nums)}")
        elif o == "Subtract":
            ans0 = nums[0]
            for num in nums[1:]:
                 ans0 -= num
            print(f"Result: {ans0}")
        elif o == "Multiply":
            print(f"Result: {math.prod(nums)}")
        else:    
            try:
                    ans1 = nums[0]
                    for num in nums[1:]:
                         ans1 /= num
                    print(f"Result: {ans1:.3f}")
            except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()