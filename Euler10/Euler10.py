import time

start = time.time()

def isprime(primenumber):
    if primenumber % 2 == 0:
        return False
        quit()
    i = 3
    while i <= primenumber/2:
        if primenumber % i == 0:
            return False
            break
        i += 2
    else:
        return True

def sumprimes(num):
    sum = 0
    x = 2
    for x in range(2,num):
        if isprime(x) == True:
            sum += x
            print("Summed" + " " + str(x))
            print("The result is " + str(sum))
    print(sum)

sumprimes(10000)

elapsed = (time.time() - start)

print "%s found in %s seconds" % ("products",elapsed)
