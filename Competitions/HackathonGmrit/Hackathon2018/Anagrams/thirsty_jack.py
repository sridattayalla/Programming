# input collect here
t, r = input().split(" ")
req_Cap = int(r)
list = [int(x) for x in input().split(" ")]

min_cost = 0
min_bottles = []

for i in range(len(list) - 1, -1, -1 ):
    if(i == len(list) - 1):


def cost(pos):
    temp = req_Cap
    temp_min_bottles = []
    temp_min_cost = 0
    while pos >= 0:
        cap = temp//(2**pos)
        temp = temp % (2**pos)
        temp_min_bottles.append(str(2**pos)+":"+str(cap))
        temp_min_cost += cap * list[pos]
        pos -= 1
    if(temp_min_cost < min_cost)



