list = [int(x) for x in input().split(" ")]

for i in range(len(list) - 1):
	min = list[i]
	for j in range(i+1, len(list), 1):
		if(min > list[j]):
			list[i] = list[j]
			list[j] = min

print(list)

# complexity:
# 0(N2)