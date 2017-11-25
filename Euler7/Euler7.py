def isprime(primenumber):
    i = 2
    while i < primenumber:
        if primenumber % i == 0:
            return False
            break
        i += 1
    else:
        return True

def main(num):
    prime_count = 1
    ii = 3
    while prime_count < num:
        if isprime(ii) == True:
            prime_count += 1
            print(prime_count)
        ii += 1
    else:
        print("Last prime is " + str(ii-1))

main(10001)
