import math

a = [str(i) for i in range(1,1000000)]
a = ''.join(a)
b = [0,9,99,999,9999,99999,999999]

product = 1
for n in b:
	product *= int(a[n])
print(product)
