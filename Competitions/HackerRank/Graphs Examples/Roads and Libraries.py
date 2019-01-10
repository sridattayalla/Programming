import sys
t = int(input())
for _ in range(t):
    graph = {}
    n, m, lib, road = map(int, sys.stdin.readline().split())
    for i in range(1,n+1):
        graph[i] = []
    for roads in range(m):
        c1, c2 = map(int, sys.stdin.readline().split())
        graph[c1].append(c2)
        graph[c2].append(c1)


    groups = []
    while(len(graph) > 0):
        keys = list(graph.keys())
        startKey = keys[0]
        visited = []
        visited.append(startKey)
        q = [startKey]
        temp_group = [startKey]
        while(len(q) >0):
            currVert = q.pop(0)
            for each in graph[currVert]:
                if(each not in visited):
                    visited.append(each)
                    q.append(each)
                    temp_group.append(each)
            del graph[currVert]
        groups.append(temp_group)

    total_cost = 0
    for each in groups:
        if(((len(each)-1)*road)+lib <= len(each)*lib):
            total_cost += ((len(each)-1)*road)+lib
        else:
            total_cost += len(each)*lib
    print(total_cost)
