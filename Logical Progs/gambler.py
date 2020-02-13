"""Simulate a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out."""

import random

def gambler(n,stack,goal):
    bets = 0; wins = 0; loss = 0; count = 0   # Initializing bets, wins, loss and count with 0.

    for i in range(n):

        # run program until stack reaches 0, stack less than goal and trails less than 0.
        while (stack > 0 and stack < goal and n > 0):
            bets += 1                   # bet = $1

            # when the value is less than 0.5, stack increments with bet and win is incremented
            if (random.random() < 0.5):
                stack += bets
                wins += 1
            
            # when the value is greater than 0.5, stack decrements with bet and loss is incremented
            else:
                stack -= bets
                loss += 1
            count += 1

    # results
    print("wins:",wins)
    print("win%: ",(wins*100)/count)
    print("loss%: ",(loss*100)/count)

n = int(input("Number of trails: "))
stack = int(input("Enter stack amount: "))
goal = int(input("Enter goal amount: "))

gambler(n,stack,goal)