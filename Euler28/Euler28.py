running_sum = 1
n = 1
delta = 0
i = 1
while (delta*(0.5) +1) <= 501:
	print(delta*(0.5) +1, n, running_sum)
	if (i-1) % 4 == 0:
		delta += 2
	n += delta
	running_sum += n
	i += 1
