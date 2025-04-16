# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
# Here's a sample run of the program (user input is in bold italics):
# Please enter an integer to be divided: 5
# Please enter an integer to divide by: 3
# The result of this division is 1 with a remainder of 2

def main():
    dividend : int = int(input("Please enter an integer to be devided: "))  # 
    divisor : int = int(input("Please enter an integer to divided by: "))  # 

    division : int = dividend // divisor  # for a exact division from given value of 1st and 2nd.
    remainder : int = dividend % divisor  # for getting result in remainder(modulus)

    print("The result of this division is " + str(division) + " with a remainder of " + str(remainder))


if __name__ == "__main__":
    main()