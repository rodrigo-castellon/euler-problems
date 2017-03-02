# ~44 seconds
import time

start = time.time()

def findlength(initial_num):
    num = initial_num
    count = 1
    while num != 1:
        count += 1
        if num % 2 == 0:
            num = num/2
        else:
            num = (3 * num) + 1
    else:
        return count

def main(ceiling):
    i = 1
    max = 1
    max_num = 1
    for i in range(1, ceiling):
        print(i)
        if findlength(i) >= max:
            max = findlength(i)
            max_num = i
    else:
        print("Max number of steps: " + str(max))
        print("Number with max number of steps: " + str(max_num))

main(1000000)

elapsed = (time.time() - start)

print("%s found in %s seconds" % ("products",elapsed))
