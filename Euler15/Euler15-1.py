import math
import time

start = time.time()

def route_num(n):
	print(math.factorial(n*2)/(math.factorial(n)**2))

route_num(20)