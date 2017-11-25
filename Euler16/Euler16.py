

a = str(2**1000)

charlist = []
for char in enumerate(a):
	print(char)
	charlist.append(int(char[1]))

print(charlist)

print(sum(charlist))