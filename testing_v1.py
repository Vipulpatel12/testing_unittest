# Function to add two numbers
def add(num1, num2):
    if num1 != None and num2 != None:
    
        return num1 + num2

# Function to subtract the second number from the first
def subtract(num1, num2):
    if num1 != None and num2 != None:
        return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    if num1 != None and num2 != None:
    
        return num1 * num2

# Function to divide the first number by the second
def divide(num1, num2):
    # Check if the divisor is zero to avoid division by zero error
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

# Calculator function that performs an operation based on user choice
def calculator(choice, num1, num2):
    """
    Parameters:
    - choice: str, representing the operation ('1' for add, '2' for subtract, '3' for multiply, '4' for divide)
    - num1: first number (int or float)
    - num2: second number (int or float)

    Returns:
    - A formatted string showing the operation and result
    """
    if choice == '1':
        return f"{num1} + {num2} = {add(num1, num2)}"
    elif choice == '2':
        return f"{num1} - {num2} = {subtract(num1, num2)}"
    elif choice == '3':
        return f"{num1} * {num2} = {multiply(num1, num2)}"
    elif choice == '4':
        return f"{num1} / {num2} = {divide(num1, num2)}"
    else:
        # Raise an error if an invalid operation choice is provided
        raise ValueError("Invalid choice")

# Run some example test cases if the script is executed directly
if __name__ == "__main__":
    print(calculator('1', 10, 5))  # Should print: 10 + 5 = 15
    print(calculator('2', 10, 5))  # Should print: 10 - 5 = 5
    print(calculator('3', 10, 5))  # Should print: 10 * 5 = 50
    print(calculator('4', 10, 5))  # Should print: 10 / 5 = 2.0
