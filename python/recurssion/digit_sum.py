ip1 = [int(x) for x in input().split(" ")]

#without recursion
'''
def D(y, t):
    if (y * t // 10 == 0) :
        return y
    else:
        return D(sum(int(x) for x in str(y)) * t, 1)
		'''
#with recursion
def sum(n):
	if n // 10 == 0 :
		return n % 10
	else :
		return (n % 10) + sum(n // 10)

def D(n, t) :
	if n // 10 == 0 :
		return n
	else:
		return D(sum(n * t), 1)
		
print(D(ip1[0], ip1[1]))