"Print the Euclidean distance from the point (x, y) to the origin (0, 0)."

from math import sqrt

def distance(x,y):

    # euclidean distance formula = sqrt(x*x + y*y).
    dist = x*x + y*y
    return sqrt(dist)

x= int(input("Enter an integer x: "))
y= int(input("Enter an integer y: "))
print(distance(x,y))