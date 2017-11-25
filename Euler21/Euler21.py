import math

def find_divisors(num):
	divisors = [1]
	for i in range(2, int(round(math.sqrt(num))+1)):
		if num % i == 0:
			divisors.append(i)
			divisors.append(num/i)
	return divisors

def d(num):
	divisors = find_divisors(num)
	return sum(divisors)

amicable_nums = []
for i in range(2, 10000):
	a = i
	b = d(a)
	if d(b) == a and a != b:
		amicable_nums.append(i)
print(amicable_nums)
print(sum(amicable_nums))