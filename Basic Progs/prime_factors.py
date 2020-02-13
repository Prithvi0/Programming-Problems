"Print the prime factors of number"

def prime_factors(num):

    pf = list()                     # Empty list 
    
    for i in range(2, num + 1):     # checking from 2
    
        while num % i == 0:         # check until the number's remainder is 0
            pf.append(i)            # appending the obtained number to the empty list
            num = num // i          # dividing the number to check further
    
        # prime number starts with 2 and so the prime factor
        if num == 1:                # if the number is 1, returns none.
            return pf

num = int(input("Enter an integer to find its prime factors: "))
print(prime_factors(num))