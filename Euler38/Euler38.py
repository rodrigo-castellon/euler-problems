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

def gen_concat(num):
	if len(str(num)) > 9:
		return 0
	i = 1
	gen_num = ''
	while True:
		if len(str(gen_num)) > 9:
			return 0
		if len(str(gen_num)) == 9:
			return int(gen_num)
		gen_num += str(num*i)
		i += 1

i = 1
largest_i = 1
largest_gen_num = 1
while True:
	if i % 10000 == 0:
		print(i)
	gen_num = gen_concat(i)
	if is_pandigital(gen_num) and gen_num > largest_gen_num:
		largest_gen_num = gen_num
		largest_i = i
		print('new largest gen num found {} from {}'.format(largest_gen_num,largest_i))
	i += 1
