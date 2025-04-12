

def main():
    dividend : int = int(input("Please enter an integer to be devided: "))  # 
    divisor : int = int(input("Please enter an integer to divided by: "))  # 

    division : int = dividend // divisor  # for a exact division from given value of 1st and 2nd.
    remainder : int = dividend % divisor  # for getting result in remainder(modulus)

    print("The result of this division is " + str(division) + " with a remainder of " + str(remainder))


if __name__ == "__main__":
    main()