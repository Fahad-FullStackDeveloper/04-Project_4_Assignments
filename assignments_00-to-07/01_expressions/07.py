# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MINUTES_PER_HOUR : int = 60
SECONDS_PER_MINUTE : int = 60

def main():
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + " seconds in a year!")
    
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR) + " minutes in a year!")

    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY) + " hours in a year!")
    
    print("There are " + str(DAYS_PER_YEAR) + " days in a year!")


if __name__ == "__main__":
    main()