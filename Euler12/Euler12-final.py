# ~10 seconds

import math
import time

start = time.time()

def num_divisible(num,divisible_count=2): #Find every divisor of num by iterating through [2,sqrt(num)) and counting twice each time
    for ii in range(2,int(math.ceil(math.sqrt(num)))):
        if num % ii == 0 and ii == 2:
            divisible_count += 2
        elif num % ii == 0:
            divisible_count += 2
    else:
        return divisible_count


def findmax(number_of_divisors): #Find the first triangle number that has a greater number of divisors than number_of_divisors
    log = []
    jj = 1
    while num_divisible((jj*(jj+1)/2)) < number_of_divisors:
        print(jj)
        jj += 1
    else:
        print("Final answer is: " + str(jj) + " with " + str(num_divisible((jj*(jj+1)/2))) + " numbers in the sequence")

findmax(500)

elapsed = (time.time() - start)

print "%s found in %s seconds" % ("products",elapsed)
