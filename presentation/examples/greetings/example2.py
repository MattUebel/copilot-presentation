# Example 2: Demonstrating another feature of GitHub Copilot Workspace

def greet(name: str) -> str:
    """
    Function to greet a person by name.
    """
    return f"Hello, {name}!"

def farewell(name: str) -> str:
    """
    Function to bid farewell to a person by name.
    """
    return f"Goodbye, {name}!"

def main(name: str):
    """
    Main function to demonstrate greeting and farewell.
    """
    print(greet(name))
    print(farewell(name))

if __name__ == "__main__":
    main("Alice")
