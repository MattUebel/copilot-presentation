# Example 4: Demonstrating a feature of GitHub Copilot Workspace

def celsius_to_fahrenheit(celsius):
    """
    Function to convert Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Function to convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9

def main():
    """
    Main function to demonstrate the temperature conversion functions.
    """
    celsius = 25
    fahrenheit = 77

    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")

if __name__ == "__main__":
    main()
