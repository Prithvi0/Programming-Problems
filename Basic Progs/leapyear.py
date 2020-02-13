"Print the year is a Leap Year or not."

def leapyear(year):

    # 4-digit year 
    if len(year) == 4:
        
        # Every 4 years is a leap year except exactly divided by 100 (e.g. 2100, 2200)
        if ((int(year) % 4 == 0 or int(year) % 400 == 0) and int(year) % 100 != 0):

            # if above condition is true, returns Leap year 
            return "Leap Year"

        return "Not a Leap Year"

    return "Enter a 4-Digit Year"

year = input("Enter a 4-Digit Year: ")
print(leapyear(year))