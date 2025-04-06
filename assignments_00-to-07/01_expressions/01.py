import random

# Number of sides on each die to roll
NUM_SIDES = 6
def roll_dice():
    """Simulates rolling a single die."""
    die1 : int = random.randint(1, NUM_SIDES)
    die2 : int = random.randint(1, NUM_SIDES)
    total : int = die1 + die2
    print("Total of two dice:" , total)

# Function to calculate the probability of rolling a specific number on a die
def main():
    die1 : int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == "__main__":
    main()