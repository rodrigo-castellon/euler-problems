import time
import math

def p_diff(n,diff):
	return (-diff - 3*diff**2 + 6*diff*n)/2

def p_sum(n,diff):
	return (6*n**2 - 2*n - 6*n*diff + 3*diff**2 + diff)/2

def is_penta(n):
	if (1+math.sqrt(1+24*n)) % 6 == 0:
		return True
	else:
		return False

thousands_num = 0
while True:
	for i in range(thousands_num*1000,thousands_num*1000+1000):
		for j in range(1,i):
			pdiff, psum = p_diff(i,j), p_sum(i,j)
			if is_penta(pdiff) and is_penta(psum):
				print('pdiff: {}; pairs of numbers: {} and {}'.format(pdiff, i,i-j))
	thousands_num += 1


