import time

start = time.time()
import math
def insert(num,list):
    count = 0
    print(list)
    list.append(num)
    list.sort()
    print(list)




def main(end_num):
    composites = [] #List of composites to skip over
    prime = 2 #current prime
    sum = 0 #sum of primes
    while prime in range(2,end_num): #Going through all primes in range
        for y in range(1,int(end_num/prime)+1):
            #Building the composite list for each prime, where y is counting between 1 and end_num/2, so y*prime is inserted up to end_num
            if y == 1: #If the for loop just started, add the prime to the sum
                sum += prime
                print(sum)
            else: #If the for loop is ongoing (after prime summed), add all multiples in range of the prime to the list of composites and establish new prime #
                list_count = 0
                if len(composites) == 0: #If prime = 2 and it is the very beginning of the entire program
                    composites.insert(0,2)
                else:
                    while y*prime > composites[list_count]:
                        list_count += 1
                    else:
                        if len(composites) != composites[list_count+1]:
                            composites.insert(len(composites),y*prime)
                        composites.insert(list_count,y*prime)
                        print(composites)

#main(100)
list = [2,4,6,8,10,12,14,16,18,20,22,24]
print(len(list))
print(list[len(list)-1])
insert(23,list)
