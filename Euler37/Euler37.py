import time


def isprime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i += 6
	return True

def get_possibilities(num):
	array = [num]
	if len(str(num)) == 1:
		return array
	index = 1
	num_string = str(num)
	while index < len(str(num)):
		array.append(int(num_string[index:]))
		array.append(int(num_string[:index]))
		index += 1
	return array
solution_list = []
j = 10
while True:
	if j % 10000 == 0:
		print(j)
	if len(solution_list) == 11:
		break
	num_array = get_possibilities(j)
	found = True
	index = 0
	while index < len(num_array):
		if not isprime(num_array[index]):
			found = False
			break
		index += 1
	if found == False:
		j += 1
		continue
	last_found_time = time.time()
	solution_list.append(j)
	j += 1

print(sum(solution_list))
