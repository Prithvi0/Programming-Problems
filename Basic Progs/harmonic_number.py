"Print the Nth harmonic number: 1/1 + 1/2 + ... + 1/N"

def har(number):

    # Initializing num to 0
    num = 0
    
    for i in range(1,number+1):
        num += 1/i                  # adding the number by 1/i
    
    return num

number = int(input("Enter an integer to find the nth Harmonic number: "))
print(har(number))