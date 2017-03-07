#~0.001 seconds
import time
start = time.time()

def main(num,ii=0):
    original = num
    list = [y for y in range(2,21)]
    while num % list[ii] != 0 and ii < len(list):
        num += original
    else:
        print("%s is divisible by %s" % (str(ii+2), str(num)))
        if (ii + 2) < 20: main(num,(ii+1))

main(2520)

elapsed = time.time()-start

print("%s found in %s seconds" % ("products",elapsed))
