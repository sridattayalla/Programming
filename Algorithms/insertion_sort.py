list = [ int(x) for x in input().split(" ") ]

def sort():
	for i in range(len(list) - 1) :
		if list[i] > list[i+1]:
			if i == 0 :
				insert(i, list[i + 1])
				del list[i + 2]
			else :
				for j in range( i - 1, -1, -1) :
					if j == 0 and list[i + 1] <= list[j]:
						list.insert(j, list[i + 1])
						del list[i + 2]
					elif list [i + 1] > list [j] :
						list.insert(j + 1, list[i + 1])
						del list[i + 2]
						break
	return list

print(sort())	
		