def largest_prime(number):
    i = 2
    while i <= (number/2):
        if (number/i) % 1 == 0:
            print(number/i)
        i += 1
    else:
        print("Number is prime")

largest_prime(50)
