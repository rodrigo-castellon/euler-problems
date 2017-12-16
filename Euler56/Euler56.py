def digits(num):
	return [int(x) for x in list(str(num))]
def d_sum(num):
	return sum(digits(num))

a,b = 1,1
max_sum = 0
while a < 101:
	b = 1
	while b < 101:
		if d_sum(a**b) > max_sum:
			max_sum = d_sum(a**b)
		b += 1
	a += 1

print max_sum
