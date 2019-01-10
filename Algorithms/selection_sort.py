list = [55, 4, 2, 17, 1, 3]

for i in range(6):
	minimum = i
	for j in range(i, 6):
		if list[minimum] > list[j]:
			minimum = j
	list[i], list[minimum] = list[minimum], list[i]

print(list)