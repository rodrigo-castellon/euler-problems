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

def gen_primes(n):
	prime_list = []
	num = 2
	while num < n:
		is_prime = True
		for index, prime in enumerate(prime_list):
			if num % prime == 0:
				is_prime = False
				break
		if is_prime == True:
			prime_list.append(num)
		num += 1
	return prime_list

def is_written(n):
	primes = gen_primes(n)
	for index, prime in enumerate(primes):
		square_num = 1
		while square_num*square_num < n:
			if prime + 2*square_num*square_num == n:
				return True
			square_num += 1
	return False

odd_composite = 33
while True:
	if odd_composite % 10000:
		print(odd_composite)
	while isprime(odd_composite):
		odd_composite += 2
	if not is_written(odd_composite):
		print('{} cannot be written as a sum of a prime and two times a square'.format(odd_composite))
	odd_composite += 2
