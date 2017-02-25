#def find_divisible(number,important):

'''
def main(starting_number)
    ii = starting_number
    important_numbers = [11, 13, 16, 17, 19]
    for x in range(0,5):
        while(ii % important_numbers[x] != 0 and x < len(important_numbers)):
            ii = ii + starting_number
            print(ii)
        if starting_number % important_numbers[x] == 0:
            print(important_numbers[x])
            if num != 19:
                starting_number = starting_number + ii
'''

def main(starting_number):
    list = [x for x in range(11,21)]



main(2520)

#This is Adrian's code
'''
def func():
    return funch(2520)

def funch(x):
    list = [y for y in range(11,21)]
    i = 0
    while(i < len(list) and (x % list[i]) == 0):
        if(i == 10):
            print(x)
        i += 1
    print(x)
    return funch(x+2520)

funch(2520)
'''
