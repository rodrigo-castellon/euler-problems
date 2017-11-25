import math

num = math.factorial(100)

running_sum = 0
for i in range(len(str(num))):
	running_sum += int(str(num)[i])

print(running_sum)