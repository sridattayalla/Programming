t= input()
a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]
max_i = 0
max_j = 0
max_sum = 0

def sum_of(i, j):
    if(i == j):
        return a[i]
    elif(i < j):
        return a[i] + a[j] + sum(b[i+1:j])
    else:
        return a[i] + a[j] + sum(b[i+1:len(b)]) + sum(b[0:j])

for i in range(len(a)):
    for j in range(len(a)):
        if(i == j and j == 0):
            max_i = 0
            max_j = 0
            max_sum = sum_of(i, j)
        else:
            if (sum_of(i, j) > max_sum):
                max_i = i
                max_j = j
                max_sum = sum_of(i, j)


print(str(max_i + 1) + " " + str(max_j + 1) + " " + str(max_sum))
