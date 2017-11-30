def gen_perm(array):
	done = False
	perm_array = []
	count = 0
	while not done:
		temp_array = array
		count += 1
		if count == 1000000:
			return [str(i) for i in temp_array]
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

original_sequence = [i for i in range(10)]

permutations = gen_perm(original_sequence)

print(int(''.join(permutations)))
