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