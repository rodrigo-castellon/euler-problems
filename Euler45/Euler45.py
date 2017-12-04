import math
def is_penta(n):
	if (1+math.sqrt(1+24*n)) % 6 == 0:
		return True
	else:
		return False

def is_tri(n):
	if (1+math.sqrt(1+8*n)) % 2 == 0:
		return True
	else:
		return False

def is_hex(n):
	if (1+math.sqrt(1+8*n)) % 4 == 0:
		return True
	else:
		return False
num = 1
while True:
	if is_penta(num) and is_tri(num) and is_hex(num):
		print('found one: {}'.format(num))
	num += 1
