def main():
    # Get the 3 sides of length of the triangle
    side1 : float = float(input("What is the length of side 1?"))
    side2 : float = float(input("What is the length of side 2?"))
    side3 : float = float(input("What is the length of side 3?"))

    # Calculate total perimeter of the triangle
    print("The permeter of the triangle is: " + str(side1 + side2 + side3))

if __name__ == '__main__':
    main()