# We will prompt user for a year and set a secondary variable to hold this value, since we are going to modify 'year'
year = int(input("Year: "))
original = year

# We will add a year right away in case the user types a leap year. We don't want to simply get that value, but the next leap year instead.
while True:
    year += 1

    # A year is leap if it can be divided by 4 with no residue. However, a secondary condition must be met:
    # If the year can be exactly divided by 100, it has to be exactly divided by 400 too!
    # Once one of these two conditions is true, the while loop will break
    if year % 4 == 0 and (year % 100 != 0 and year % 400 != 0):
        break
    elif year % 100 == 0 and year % 400 == 0:
        break
        
# Now, our 'original' variable will come in handy. 
# We can simply print our statement and let our user know when will the next leap year be!
print(f"The next leap year after {original} is {year}")
