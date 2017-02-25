import time

start = time.time()

def multiple(x,y):
	i = 1
	xList = []
	yList = []
	zList = []
	while i*x < 1000:
		xList.insert(i - 1, i*x)
		i += 1
	else:
		xSum = (sum(xList))
	i = 1
	while i*y < 1000:
		if((i*y) not in xList):
			yList.insert(i - 1, i*y)
		i += 1
	else:
		ySum = (sum(yList))
#	i = 1
#	z = 15
#	while i*z < 1000:
#		zList.insert(i - 1, i*z)
#		i += 1
#	else:
#		zSum = (sum(zList))
	print (xSum + ySum)
multiple(3,5)

elapsed = (time.time() - start)

print "%s found in %s seconds" % ("answer",elapsed)
