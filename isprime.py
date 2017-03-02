def isprime(primenumber):
    i = 2
    while i < primenumber/2:
        if primenumber % i == 0:
            return False
            break
        i += 1
    else:
        return True
