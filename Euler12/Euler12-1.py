import math
import time

start = time.time()

def isprime(primenumber):
    i = 2
    while i < (math.sqrt(primenumber)):
        if primenumber % i == 0:
            return False
            break
        i += 1
    else:
        return True

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def is__prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return sieve


print [2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(10000000)) if v and i>0]



'''
def pfactor_to_value(lst):
    pfactors = [[],[]] #create pfactors, where pfactors[0] is count and pfactors[1] are the actual prime factors
    for prime_factor in lst:
        if not prime_factor in pfactors[1]: #if not i in pfactors: If this item has not been documented before
            pfactors[1].append(prime_factor)
            pfactors[0].append(1)
            #print(pfactors)
        else:
            pos = pfactors[1].index(prime_factor) #Index the list to find where it is
            pfactors[0][pos] += 1
    return pfactors


def prime_factors(num,prime_count=0,lst=[]):
    ii = 2
    while ii < (num/2 + 1):
        if (isprime(ii) == True) and num % ii == 0: #If this number is a prime factor...
            #Add this prime factor to the list
            lst.append(ii)
            #Debugging
            print("Prime factor: " + str(ii))
            #Simplify
            num = num/ii
            #Add count
            prime_count += 1
        else:
            ii += 1
        print(ii)
    else:
        if isprime(num) == False:
            return (prime_factors(num,prime_count,lst))
        elif num == 1:
            lst_pls1 = [(x+1) for x in pfactor_to_value(lst)[0]]
            product = 1
            for item in lst_pls1:
                product *= item
            return product
        else:
            lst.append(num)
            #Compute divisor count based on the prime factors
            lst_pls1 = [(x+1) for x in pfactor_to_value(lst)[0]] #Make a new list with each term being += 1
            #Multiply all items in list lst_pls1
            product = 1
            for item in lst_pls1:
                product *= item
            return product
'''



print(sieve_for_primes_to(2340872384237))


#print(prime_factors(38628972))






elapsed = time.time()-start

print "%s found in %s seconds" % ("products",elapsed)
