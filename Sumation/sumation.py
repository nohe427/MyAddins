def sumat(num):
	x=float(num/2.0)
	y=float(num+1)
	i=0
	for j in range(0, num+1):
		i=i+j
	return "{0}, {1}".format(float(x*y), i)
