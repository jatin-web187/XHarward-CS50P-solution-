# interpreter.py

def main():
    # Prompt user for input and split into components
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    # Convert x and z to integers and evaluate based on y
    n1 = float(x)
    n2 = float(z)

    if y == "+":
        result = n1 + n2
    elif y == "-":
        result = n1 - n2
    elif y == "*":
        result = n1 * n2
    elif y == "/":
        # Assumes n2 is not 0
        result = n1 / n2

    # Output formatted result
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
