# x = 5 
# x = 'gary'
# int x =5
# (cp)def int x = 5

cpdef int test(int x):
	cdef int y = 0
	cdef int i
	for i in range(x):
		y += i
	return y	
