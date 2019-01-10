def decode(str):
	if len(str) <= 1:
		return 1
	elif str[0] == "0":
		return 0
	elif int(str[0 : 2]) <= 26:
		return decode(str[1 : len(str)]) + decode(str[2 : len(str)])
	else:
		return decode(str[1 : len(str)])
		
print(decode("111"))
'''
aaa
ak
ka
 '''