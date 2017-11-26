import math

running_sum = 0
num = 3
while True:
	fact_sum = sum([math.factorial(int(x)) for x in list(str(num))])
	if fact_sum == num:
		running_sum += num
		print(running_sum, num)
	num += 1
