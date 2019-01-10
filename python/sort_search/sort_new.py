list = [int(x) for x in input().split(" ")]

def swap_pos(i, j):
	less = list[j]
	great = list[i]
	list[i] = less
	list[j] = great
	
for i in range(len(list) - 1):
	if(list[i] > list[i+1]):
		swap_pos(i, i+1)
		pos = i - 1
		while pos > 0:
			if(list[pos] > list[pos+1]):
				swap_pos(pos, pos+1)
			pos -= 1
				
print(list)