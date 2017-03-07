#~0.0002 seconds
import time
start = time.time()

def main(num):
    orig_list = [y for y in range(1,num + 1)]
    square_list = []
    ii = 0
    while ii < (len(orig_list)):
        square = orig_list[ii]**2
        square_list.insert(ii,square)
        ii += 1
    print(square_list)
    print(abs(sum(square_list) - ((sum(orig_list)**2))))

main(100)

elapsed = time.time() - start

print("%s found in %s seconds" % ("products",elapsed))
