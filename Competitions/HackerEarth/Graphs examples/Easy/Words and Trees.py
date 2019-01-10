import sys
N, Q = map(int, sys.stdin.readline().split())
characters = [x for x in input().split(" ")]
branches = {}
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    if(u not in branches):
        branches[u] = [v]
    else:
        branches[u].append(v)
    if(v not in branches):
        branches[v] =[u]
    else:
        branches[v].append(u)

for _ in range(Q):
    num_str, T = map(str, sys.stdin.readline().split())
    num = int(num_str)
    have = characters[num-1]
    for each in branches[num]:
        have = have+characters[each-1]
    count = 0
    print(have)
    for x in T:
        if(x not in have):
            # print(x)
            count += 1
    print(count)

