# input segment
# str_m, str_n = input().split(",")
m = 3
n = 7
matrix = [[7,6,-4,-8,5,-1,3],[1,3,-2,-10,4,2,9], [11,9,8,17,-3,0,-3]]

# for _ in range(m+1):
#     matrix.append([int(x) for x in input().split(",")])
# print(matrix)

# calculating sum at counters and inserting them in a list
# if sum at counters is negative don't place a counter over there
Totals = []
  #if counters at corners of matrix
if matrix[0][0] >=0 :
    Totals.append([[0],matrix[0][0]])
if matrix[0][n-1] >=0 :
    Totals.append([[n-1], matrix[0][n-1]])
if matrix[m-1][0] >=0 :
    Totals.append([[(m -1)*(n)], matrix[m-1][0]])
if matrix[m-1][n-1] >=0 :
    Totals.append([[m*(n) -1], matrix[m-1][n-1]])
  #if counters at sides
for i in range(1, n):
    if(matrix[0][i-1] + matrix[0][i] >= 0):
        Totals.append([[i-1, i], matrix[0][i-1] + matrix[0][i]])
    if(matrix[m-1][i-1] + matrix[m-1][i] >= 0):
        Totals.append([[(m-1)*n + i - 1, (m-1)*n + i], matrix[m-1][i-1] + matrix[m-1][i]])
for i in range(1, m):
    if (matrix[i-1][0] + matrix[i][0] >= 0):
        Totals.append([[(i-1)*n, i*n], matrix[i-1][0] + matrix[i][0]])
    if (matrix[i-1][n-1] + matrix[i][n-1] >= 0):
        Totals.append([[i*n-1, (i+1)*n-1], matrix[i - 1][n - 1] + matrix[i][n - 1]])
  #if counters at 4 block intersection
for i in range(m-1):
    for j in range(n-1):
        s = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        if(s >=0):
            blocks = [(i*n)+j, (i*n)+j+1, (i+1)*n+j, (i+1)*n+j+1]
            Totals.append([blocks, s])


# max sum that got in recurssion will take as answer
def max_total(selected, totals):
    max_val = 0
    if(len(totals) == 0):
        max_val = 0
    else:
        for i in range(len(totals)):
            temp = totals[i][0]
            temp_val = totals[i][1]

            if(not any([x in selected for x in temp])):
                if max_val < temp_val + max_total(selected+temp, totals[i+1:]):
                    max_val = temp_val + max_total(selected+temp, totals[i+1:])


    return max_val

# output segment
print(max_total([], Totals))



