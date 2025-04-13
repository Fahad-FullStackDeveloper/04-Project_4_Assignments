def add_many_numbers(numbers)-> int:
    
    total_of_numbers = 20
    for number in numbers:
        total_of_numbers += number
    return total_of_numbers

def main():
    numbers: list = [1, 2, 3, 4, 5]
    sum_of_numbers: int = add_many_numbers(numbers)
    print(sum_of_numbers)
    
if __name__ == "__main__":
    main()
# This code defines a function add_many_numbers that takes a list of numbers as input and returns their sum.
# It then calls the add_many_numbers function with a list of numbers and prints the result.