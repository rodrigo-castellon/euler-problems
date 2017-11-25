one_to_twenty_dict = {
	0: 0,
	1: 3, 
	2: 3, 
	3: 5, 
	4: 4, 
	5: 4, 
	6: 3, 
	7: 5, 
	8: 5, 
	9: 4, 
	10: 3, 
	11: 6, 
	12: 6, 
	13: 8, 
	14: 8, 
	15: 7, 
	16: 7, 
	17: 9, 
	18: 8,
	19: 8
}

tens_dict = {
	2: 6,
	3: 6,
	4: 5,
	5: 5,
	6: 5,
	7: 7,
	8: 6,
	9: 6
}

def count_letters(num):
	num_string = str(num)
	if num == 1000:
		return 11
	if len(num_string) == 3:
		if num % 100 == 0:
			return one_to_twenty_dict[int(num_string[0])] + 7
		else:
			return count_letters(int(num_string[1:])) + one_to_twenty_dict[int(num_string[0])] + 10
	elif len(num_string) == 2:
		if num < 20:
			return one_to_twenty_dict[num]
		else:
			return count_letters(int(num_string[1:])) + tens_dict[int(num_string[0])]
	elif len(num_string) == 1:
		return one_to_twenty_dict[num]

num_letters_list = []
for i in range(1,1001):
	num_letters_list.append(count_letters(i))


print(sum(num_letters_list))