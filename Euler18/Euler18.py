file = open('numbers.txt')
file_content = file.readlines()

def insert_space(string, index):
    return string[:index] + ' ' + string[index:]

for index, elem in enumerate(file_content):
	elem = ''.join(x for x in elem if x.decode('utf-8').isdecimal())
	for i in range(len(elem)/2-1):
		elem = insert_space(elem, 3*i+2)
	elem = elem.split()
	elem = [int(i) for i in elem]
	file_content[index] = elem

def evaluate(pyramid_list, path_list):
	current_sum = 75
	current_pos = 0
	for i in range(14):
		current_pos += path_list[i]
		current_sum += pyramid_list[i+1][current_pos]
	return current_sum

binary_array = [0 for i in range(14)]
def convert(num,binary_array):
	subtract_num = 0
	i = 0
	while 2**i <= num:
		subtract_num = 2**i
		i += 1
	new_num = num - subtract_num
	binary_array[-i] = 1
	if new_num > 0:
		return convert(new_num, binary_array)
	else:
		return binary_array

max_num = 0
max_path = [0 for i in range(14)]
for i in range(2**14):
	binary_array = [0 for x in range(14)]
	binary_array = convert(i, binary_array)
	evaluation = evaluate(file_content, binary_array)
	if evaluation > 1000:
		print(i, binary_array, evaluation)
	if evaluation > max_num:
		max_num = evaluation
		max_path = binary_array

print(max_num, max_path)