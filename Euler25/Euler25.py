def fib(n):
	i = 1
	a = 1
	b = 1
	while len(str(a)) < n:
		c = a + b
		a = b
		b = c
		i += 1
	print(a, i)

fib(1000)
		
