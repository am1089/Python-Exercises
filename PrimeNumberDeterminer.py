# Determines if a number is prime or not

import math

print('Input a number')
number = input()
number = int(number)
maxfactor = int(math.sqrt(number)) + 1 # +1 for rounding.
limit = maxfactor + 1 # +1 for range() upper limit

if number <= 1:
    print(number, "is not a prime number")
else:
    for i in range(2, limit):
        # print("i=", i)
        if (number % i) == 0:
            print(number, "is not a prime number")
            break

# print("Final i=", i)
if i >= maxfactor:
    print(number, "is a prime number")
    
