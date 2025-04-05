# convertion degree from_Fahrenheit_to_Celsius
def main():
    # Prompt the user for input
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the given formula
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Print the result
    print(f"\nTemperature: {fahrenheit}F = {celsius}C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()