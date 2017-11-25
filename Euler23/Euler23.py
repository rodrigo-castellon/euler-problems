import math

def find_divisors(num):
	divisors = [1]
	for i in range(2, int(round(math.sqrt(num))+1)):
		if num % i == 0:
			divisors.append(i)
			divisors.append(num/i)
	return divisors

def typenum(num):
	if sum(find_divisors(num)) == num:
		return 'perfect'
	elif sum(find_divisors(num)) < num:
		return 'deficient'
	else:
		return 'abundant'

abundant_num_list = []

for i in range(28123):
	if typenum(i) == 'abundant':
		abundant_num_list.append(i)

def is_sum(num):
	i = 0
	while abundant_num_list[i] < num:
		j = i + 1
		while abundant_num_list[j] < num:
			if abundant_num_list[i] + abundant_num_list[j] == num:
				return True
			j += 1
		i += 1
	return False

running_sum = 0

for i in range(1, 28123):
	print('{}/{}'.format(i,28123))
	if not is_sum(i):
		running_sum += i

print(running_sum)