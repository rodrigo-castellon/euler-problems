# ~0.001 seconds

import time

start = time.time()


def largest_prime(number):
    i = 2
    while i <= (number/2):
        if (number/i) % 1 == 0:
            print(number/i)
        i += 1
    else:
        print("Number is prime")

largest_prime(50)

elapsed = time.time() - start

print "%s found in %s seconds" % ("products", elapsed)
