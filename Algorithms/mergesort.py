def merge_sort(list, l, r):
	if l < r:
		m = (l + r)//2 - 1
		temp_l = [0] * (m + 1 - l)
		temp_r = [0] * (r - m - 1)
		for i in range(len(temp_l))	:
			temp_l[i] = list[l+i]
		print(temp_l)
		merge_sort(temp_l, l, len(temp_l))
		for i in range(len(temp_r)):
			temp_r[i] = list[m + 1 +i]
		merge_sort(temp_l, m + 1, len(temp_l))
		print(temp_r)

list = [5, 2, 3, 1, 8, 4]
merge_sort(list, 0, len(list))		