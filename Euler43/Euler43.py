def gen_perm(array):
	done = False
	perm_array = []
	while not done:
		temp_array = array
		perm_array.append(temp_array)
		# STEP 1
		largestI = -1
		for index in range(len(array)-1):
			if array[index] < array[index+1]:
				largestI = index
		if largestI == -1:
			done = True
			return perm_array

		# STEP 2
		largestJ = -1
		for index, elem in enumerate(array):
			if elem > array[largestI]:
				largestJ = index

		# STEP 3
		temp_array = array[:]
		temp_array[largestI], temp_array[largestJ] = temp_array[largestJ], temp_array[largestI]
		array = temp_array

		# STEP 4
		end_array = array[largestI+1:]
		end_array = list(reversed(end_array))
		array[largestI+1:] = end_array

prime_list = [2,3,5,7,11,13,17]

def is_substring(array):
	i = 1
	substrings = []
	is_substring = True
	while i < len(array)-2:
		substring = int(str(array[i]) + str(array[i+1]) + str(array[i+2]))
		if not substring % prime_list[i-1] == 0:
			is_substring = False
			break
		i += 1
	if is_substring == True:
		return True
	else:
		return False

print('generating permutations')
pandigital_array = [0,1,2,3,4,5,6,7,8,9]
permutations = gen_perm(pandigital_array)
print('generated permutations')
running_sum = 0
for index, permutation in enumerate(permutations):
	if is_substring(permutation):
		num = int(''.join([str(x) for x in permutation]))
		running_sum += num
		print(running_sum)
print('final sum: {}'.format(running_sum))

