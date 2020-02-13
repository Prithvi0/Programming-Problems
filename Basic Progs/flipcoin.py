"Flip Coin and print percentage of Heads and Tails"

import random

def flipcoin(f):

    heads=0; tails=0                # Initially heads and tails are 0

    # coin flips
    for i in range(f):
        coin = random.random()      # generating random values

        if coin < 0.5:              # head is incremented if coin toss value is less than 0.5
            heads += 1

        else:                       # tail is incremented if coin toss value is greater than 0.5
            tails += 1

    heads_percent = float((heads * 100)/f)     # head percent
    tails_percent = float((tails * 100)/f)     # tail percent
    return "heads_percent: %.2f,tails_percent: %.2f" %(heads_percent,tails_percent)

flips= int(input("Enter the number of flips: "))
print(flipcoin(flips))