import time
start_time = time.perf_counter()
n =int(input())
for i in range(n):
    a, b = input().split(" ")
    list_size =int(a)
    frns_to_rmve =int("0")
    list = [int(x) for x in input().split(" ")]
    final_list = [list[0]]
    x = 1
    while frns_to_rmve > 0:
        if final_list [-1] < list [x]:
            final_list.pop()
            final_list.append(list[x])
            frns_to_rmve -= 1
            x += 1
        else:
            if x == len(list) - 1:
                list.pop()
                x -= x
    print(*final_list)

print(time.perf_counter() - start_time)