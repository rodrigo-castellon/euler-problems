found = []
i = 10
while True:
	print('{}: {}'.format(i,found))
	digit_sum = sum([int(x)**5 for x in list(str(i))])
	if digit_sum == i:
		print('found: {}'.format(i))
		found.append(i)
	i += 1
