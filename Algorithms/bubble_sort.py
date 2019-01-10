list = [55, 2, 5, 4, 3, 1]

for i in range(6):
	for j in range( 5 - i):
		if(list[j] > list[j+1]):
			list[j], list[j + 1] = list[j + 1], list[j]
print(list)