# Function to subtract the second number from the first
def subtract(num1, num2):
    if num1 is None or num2 is None:
        raise ValueError("Inputs cannot be None")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Inputs must be int or float")
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    if num1 is None or num2 is None:
        raise ValueError("Inputs cannot be None")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Inputs must be int or float")
    return num1 * num2

# Function to divide the first number by the second
def divide(num1, num2):
    if num1 is None or num2 is None:
        raise ValueError("Inputs cannot be None")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Inputs must be int or float")
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
    """
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    else:
        raise ValueError("Invalid choice")
# Run some example test cases if the script is executed directly
if __name__ == "__main__":
    print(calculator('1', 10, 5))  # Should print: 10 + 5 = 15
    print(calculator('2', 10, 5))  # Should print: 10 - 5 = 5
    print(calculator('3', 10, 5))  # Should print: 10 * 5 = 50
    print(calculator('4', 10, 5))  # Should print: 10 / 5 = 2.0
