import math
import time

start = time.time()


#old brute force function
def num_divisible(divisible_count,num):
    #Brute force find every divisor
    for ii in range(2,int(math.ceil(math.sqrt(num)))):
        if num % ii == 0 and ii == 2:
            divisible_count += 2
        elif num % ii == 0:
            divisible_count += 2
    else:
        return divisible_count
        #num_divisible(2)





def findmax(number_of_divisors):
    log = []
    jj = 1
    while num_divisible(2,(jj*(jj+1)/2)) < number_of_divisors:
        print(jj)
        log.append(num_divisible(2,(jj*(jj+1)/2)))
        jj += 1
    else:
        print("Final answer is: " + str(jj) + " with " + str(num_divisible(2,(jj*(jj+1)/2))) + " numbers in the sequence")
        #return jj
        #print(log)

maxes = [7]
#while kk < 100:
#    if findmax(kk) == maxes[len(maxes)-1]:
#findmax(500)



print(num_divisible(2,38628972))



elapsed = (time.time() - start)

print "%s found in %s seconds" % ("products",elapsed)

#num_divisible(2)

#1. find first divisor of original number
#2. Since the first divisor has to be prime, continue this process (recursion) with the opposite divisor, while adding 1 to the count
#3. If at any point the number is prime, add one to the count and stop.
