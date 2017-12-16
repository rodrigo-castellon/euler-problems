def digits(num):
	return [int(x) for x in list(str(num))]

multiples = [1,2,3,4,5,6]

i = 1
while True:
	found = True
	mults = digits(i)
	for index, mult in enumerate(multiples):
		if sorted(digits(i*mult)) != sorted(digits(i)):
			found = False
			break
	if found == False:
		i += 1
	else:
		print i
		break
