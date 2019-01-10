puzzle = []
words = []

'''puzzle_file = open("puzzle.txt", "r")

for line in puzzle_file:
	row_list = []
	for each in line:
		row_list.append(each)
	puzzle.append(row_list)
	
words = puzzle[len(puzzle) - 1]
del puzzle[len(puzzle) -1]
for each in puzzle:
	print(" ".join(each))

print(words)'''

#getting puzzle
for i in range(10):
	new_row = [x for x in input()]
	puzzle.append(new_row)

#getting words
words = [word for word in input().split(";")]
