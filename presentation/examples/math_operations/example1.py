# Example 1: Demonstrating a feature of GitHub Copilot Workspace

def add(a: float, b: float) -> float:
    """
    Function to add two numbers.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Function to subtract two numbers.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Function to multiply two numbers.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Function to divide two numbers.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition of {x} and {y}: {add(x, y)}")
    print(f"Subtraction of {x} and {y}: {subtract(x, y)}")
    print(f"Multiplication of {x} and {y}: {multiply(x, y)}")
    print(f"Division of {x} and {y}: {divide(x, y)}")
