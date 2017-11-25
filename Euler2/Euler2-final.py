import time

start = time.time()

def fibsum(limit,sm=0,current_count=1,last_count=1):
    temp_last = last_count
    last_count = current_count
    current_count += temp_last
    if current_count < limit:
        if current_count % 2 == 0:
            print(str(current_count) + " is even")
            sm += current_count
        fibsum(limit,sm,current_count,last_count)
    else:
        print(sm)

fibsum(4000000)

elapsed = time.time() - start

print "%s found in %s seconds" % ("products", elapsed)
