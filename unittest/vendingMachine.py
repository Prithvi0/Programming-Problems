"""There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
returned by Vending Machine. Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change"""

def vendingMachine(amount):
    
        notes = [1000, 500, 100, 50, 10, 5, 2, 1]       # Notes available
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0]             # Initially zero 
        
        # calculating minimum number of notes possible
        for i, j in zip(notes, count):

            # run until amount reaches zero
            if amount >= i:
                j = amount // i
                amount -= j * i
                print(i, ": ", j)   # notes and notes count

amount = int(input("Enter the amount to withdraw: "))
vendingMachine(amount)