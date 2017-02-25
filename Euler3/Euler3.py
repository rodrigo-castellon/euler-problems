isprime = False
def isprime(primenumber):
    i = 1
    while i < primenumber:
        if primenumber % i == 0:
            print("False")
            quit()
        i += 1
    else:
        print("True")

def greatest_factor(number):
    i = 2
    greatest_factor_1 = 1
    while i < number:
        if number % i == 0:
            greatest_factor_1 = i
        i += 1
    else:
        if isprime(greatest_factor_1) == "False":
            greatest_factor(greatest_factor_1)
        else:
            print(greatest_factor_1)
isprime(3)
