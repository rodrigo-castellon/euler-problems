i = 1
n = 0
while i < 1000:
	if i % 3 or i % 5:
		n += i
	i = i + 1
else:
	print n
