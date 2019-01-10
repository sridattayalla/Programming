import time as ti
t = int(input())
n = int(input())
ki = ti.clock()
for _ in range(t):
    list = []
    for i in range(n):
        list.append([int(x) for x in input().split(" ")])

    max_hap = list[0][0] + list[1][0] - sum([x[1] for x in list[2:len(list)]])
    for i in range(len(list)):
        for j in range(len(list)):
            if (i != j):
                temp_hap = list[i][0] + list[j][0] - sum([x[1] for x in list[0:len(list)]]) + list[i][1] + list[j][1]
                if temp_hap > max_hap:
                    max_hap = temp_hap
                    print([i, j])
    print(max_hap)
print(ti.clock()-ki)
