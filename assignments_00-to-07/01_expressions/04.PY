import math  # Import the math library for sqrt function

def main():
    ab : float = float(input("Enter the length of AB: "))
    ac : float = float(input("Enter the length of AC: "))

    # Calculate the third side of triangle(hypotenuse) using Pythagoren!
    bc : float = math.sqrt(ab ** 2 + ac ** 2)
    print("The length of BC (the hypotenuse) is: " + str(bc))


if __name__ == "__main__":
    main()