import math

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

def swap(arr, a, b):
	a_elem = arr[a]
	b_elem = arr[b]
	arr[a] = b_elem
	arr[b] = a_elem
	return arr

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

digits_orig = [1,2,3,4,5,6,7,8,9,0]
found = False
digits = digits_orig[:]
while found == False:
	digits = digits_orig[:len(digits)-1]
	a = gen_perm(digits)
	prime = 0
	for index, digits in enumerate(a):
		if digits[-1] % 2 == 0:
			continue
		num = int(''.join([str(i) for i in digits]))
		if num % 3 == 0:
			print('num {}'.format(num))
		if isprime(num):
			prime = num
			found = True
			print('larger prime found! {}'.format(prime))

print(prime)
