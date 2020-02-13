"print a table of the powers of 2"

def powers2(number):

    # powers start from 0, so, count is taken as -1
    count = -1
    
    for i in range(number+1):

        # count is incremented by 1 to start from 0th power
        count += 1
        print("2^%d" %count,"=",2**i)

number = int(input("Enter a number range to print powers of 2: "))
powers2(number)