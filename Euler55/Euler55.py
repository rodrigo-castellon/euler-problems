def digits(num):
	return [x for x in list(str(num))]

def rev_add(num):
	rev = reversed(digits(num))
	return num + int(''.join(rev))

def is_palin(num):
	num = str(num)
	i = 0
	while i < len(num)/2:
		if num[i] != num[-i-1]:
			return False
		i += 1
	return True

def is_lychrel(num):
	i = 0
	num = rev_add(num)
	while is_palin(num) != True:
		if i == 50:
			return True
		num = rev_add(num)
		i += 1
	return False
count = 0
index = 1
while index < 10000:
	if is_lychrel(index):
		count += 1
	index += 1
print count
