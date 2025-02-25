def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract second number from first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide first number by second and return the result.
    
    Raises ZeroDivisionError for division by zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    print("Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            try:
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            # Ask user if they want another calculation
            another = input("Would you like to calculate again? (yes/no): ").lower()
            if another != "yes":
                break
        else:
            print("Invalid Input. Please choose a valid option.")

if __name__ == "__main__":
    main()

