"Find the roots of the equation a*x*x + b*x + c."

from math import sqrt

def quadratic(a,b,c):

    try:
        delta = float((b*b)-(4*a*c))

        # for delta > 0, two distinct real roots are obtained
        if delta > 0:
            r1 = float(-b + sqrt(d))/(2*a)
            r2 = float(-b - sqrt(d))/(2*a)
            return "2 Distinct Real Roots: r1 = %.2f and r2 = %.2f" %(r1, r2)

        # for delta = 0, two equal real roots are obtained
        elif delta ==  0:
            r1 = r2 = float(-b/(2*a))
            return "2 Equal Real Roots: r1 = %.2f and r2 = %.2f" %(r1, r2)

        # for delta < 0, two distinct complex roots are obtained
        else:
            r = float(-b/(2*a))
            imag = float(sqrt(-delta/(2*a)))
            return "2 Distinct Complex Roots: r1 = %.2f+%.2fj and r2 = %.2f-%.2fj" %(r, imag, r, imag)

    except:
        return "Enter appropriate values"

a = float(input("Enter 'a' value: "))
b = float(input("Enter 'b' value: "))
c = float(input("Enter 'c' value: "))
print(quadratic(a,b,c))