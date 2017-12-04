import time
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
start = time.time()

LIMIT = 1000000

primes = gen_primes(LIMIT/10)
longest_consecutive = [0,0,0]

for i in range(1,len(primes)+1):
	summ = 0
	j = 0
	while summ < LIMIT and j < len(primes)+1-i:
		summ = 0
		for k in range(i):
			summ += primes[j+k]
		print(summ)
		if i > longest_consecutive[0] and summ < LIMIT and isprime(summ):
			longest_consecutive[0] = i
			longest_consecutive[1] = j
			longest_consecutive[2] = summ
		j += 1
print(str(longest_consecutive) + ' found in {} seconds'.format(time.time()-start))
