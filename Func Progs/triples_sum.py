"""A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0."""

def triples_sum(arr, n):
    
    # look for elements till n-2
    for i in range(n-2):
        
        # look for elements till n-1
        for j in range(i+1, n-1):
    
            # look for elements till n
            for k in range(j+1, n):
    
                # return numbers if sum of all 3 integers are 0.
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
    
    print("No Zero sum")

n = int(input("Enter the number of elements: "))
arr = list()                    # Empty list
print("Enter the elements: ")

# append the numbers in the list as entered by the user
for i in range(n):
    arr.append(int(input()))

triples_sum(arr,n)