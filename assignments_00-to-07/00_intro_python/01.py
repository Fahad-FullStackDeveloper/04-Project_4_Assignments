# add2numbers OR add 2 variables with total
def main():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number:")
    num1 : int = int(num1)
    num2 : str = input("Enter second number:")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")

# This line calls the main() function when the Python file is executed.
if __name__ == "__main__":
    main()