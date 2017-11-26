import math

def get_comp_fact(num):
	comp_array = []
	for i in range(1,int(round(math.sqrt(num)))+1):
		if num % i == 0:
			comp_array.append((i, num/i))
	return comp_array

def is_pandigital(num_string):
	if type(num_string) == type(5):
		num_string = str(num_string)
	if '0' in num_string:
		return False
	if len(list(num_string)) != len(set(list(num_string))):
		return False
	used_array = []
	for index, char in enumerate(num_string):
		if int(char) > len(num_string):
			return False
	return True
i = 1
running_sum = 0
while True:
	i += 1
	if i == 7254:
		print(i)
	comp_array = get_comp_fact(i)
	for index, tupl in enumerate(comp_array):
		num_string = str(tupl[0]) + str(tupl[1]) + str(i)
		if len(num_string) == 9 and is_pandigital(num_string):
			running_sum += i
			print(tupl[0],tupl[1])
			print('found! sum: {}; product: {}'.format(running_sum,i))
			break
