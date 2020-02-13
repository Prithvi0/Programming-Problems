"""Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process."""

"Calculate total random number needed to have all distinct numbers."

# import random

# def coupon_numbers(n):

#     l=list()                    # Empty list
#     Distinct_nums = 0           # Initializing Distinct numbers
   
#     while Distinct_nums == n:
#         for i in range(n*n):
#             r = random.randint(1,1000)  # Generating random numbers

#             if r not in l:          # Filtering distinct numbers
#                 l.append(r)
#                 Distinct_nums += 1
    
    
#         return Distinct_nums        # printing distinct numbers

# n = int(input("Enter the number of coupons: "))

# print(coupon_numbers(n))

import random

def coupon_numbers(n):
    
    distinct = set()                # empty set
    cnt = 0                         # setting count to 0
    
    while len(distinct) < n:        # program runs until all the distinct values are created
    
        r = random.randint(1,n)     # creating random values
        distinct.add(r)             # adding random values to distinct variable to filter out duplicates
        cnt += 1                    # incrementing the count as distinct numbers are added
    
    return cnt                      # returning count of distinct values

n = int(input("Enter the number of distinct coupons to form: "))
print(coupon_numbers(n))