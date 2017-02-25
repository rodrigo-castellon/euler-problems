import time

start = time.time()
import math

def main(end_num):
    primes = [2] #List of composites to skip over
    prime = 3 #current prime
    sum = 2 #sum of primes
    while prime in range(3,end_num): #Going through all primes in range
        for y in range(3,prime):
            if prime % y == 0:
                break
            else:
                prime = y
        else:
            sum += prime
            prime += 1
            print(prime)
        '''for y in range(0,len(primes)): #If the "prime" is divisible by any previous prime, prime += 1, otherwise add prime and continue
            if prime % primes[y] == 0:
                break
            if y == len(primes)-1:
                primes.append(prime)
                sum += prime
                break'''
        prime += 1
    print(primes)
    print(prime)
    print(sum)

main(10000)

elapsed = (time.time() - start)

print "%s found in %s seconds" % ("products",elapsed)
