"Function to print 2 Dimensional Array."

def array2d(rows, cols):

    array = list()                      # initializing an array of empty list

    print("Enter the inputs row wise")
    for i in range(rows):
        a = list()                      # rows as empty empty list
    
        for j in range(cols):
            a.append(int(input()))      # append columns as entered by the user
        array.append(a)                 # append the columns with the rows

    print("2darray: ")
    for i in range(rows):
    
        for j in range(cols):
            print(array[i][j], end=" ")     # print as a 2D Array
    
        print()

rows = int(input("Enter total number of rows: "))
cols = int(input("Enter total number of rows: "))
array2d(rows,cols)