ignore = input()
list = [int(x) for x in input().split(" ")]
op_x_list = [-1]
op_y_list = []

for i in range(1, len(list)):
    temp = i - 1;
    while (temp >= 0):
        if(list[i] < list[temp]):
            op_x_list.append(temp + 1)
            temp = -1
        elif(temp == 0 or op_x_list[temp] == -1):
            op_x_list.append(-1)
            temp = -1
        else:
            temp = op_x_list[temp] - 1

op_y_list = []
for i in range(len(list)):
    op_y_list.append(-1)

for i in range(len(list) - 1, -1, -1):
    temp = i + 1
    while(temp <= len(list) - 1):
        if(list[i] < list[temp]):
            op_y_list[i] = temp + 1
            temp = len(list)
        elif(op_y_list[temp] == -1 or temp == len(list) - 1):
            op_y_list[i] = -1
            temp = len(list)
        else:
            temp = op_y_list[temp] - 1


op_list = [ x + y for x, y in zip(op_y_list, op_x_list)]
print(*op_list)