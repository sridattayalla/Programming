num1 = int(input("num1:").strip())
num2 = int(input("num2:").strip())

def gcd(dividend, n):
	if(dividend == 0 or n == 0):
		return 0
	elif(dividend % n == 0):
		return n
	else:
		return gcd(n, dividend % n)


print(gcd(num2, num1)) if (num1 < num2) else print(gcd(num1, num2))
	