def isprime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i += 6
	return True

def quad_eval(a,b):
	n = 0
	if isprime(n**2 + a*n + b) == False:
		return 0
	while isprime(n**2 + a*n + b) == True:
		n += 1
	return n - 1

running_max = 0
runningmax_tuple = (0,0)
for i in range(2001):
	print('i: {}'.format(i))
	for j in range(2001):
		a,b = i-1000,j-1000
		evaluation = quad_eval(a,b)
		if evaluation > running_max:
			running_max = evaluation
			runningmax_tuple = (a,b)
			print(evaluation)
			print(runningmax_tuple)

print(evaluation)
print(runningmax_tuple)

print(runningmax_tuple[0] * runningmax_tuple[1])
