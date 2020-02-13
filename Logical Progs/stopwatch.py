"Measure the elapsed time between start and end"

import time

try:
    while True:
        start = int(input("Enter a number to Start: "))
        startTime = time.time()                             # program startTime
        stop = int(input("Enter a number to Stop Time: "))
        stopTime = time.time()                              # program stopTime
        elapsedTime = stopTime - startTime                  # total Time taken
        print("Elapsed time: ",elapsedTime, "secs")
        
except ValueError:
    print("Invalid input")