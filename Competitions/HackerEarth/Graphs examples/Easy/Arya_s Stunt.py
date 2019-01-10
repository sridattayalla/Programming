import sys
from collections import defaultdict
import time as t
start = t.clock()
N, M = map(int, sys.stdin.readline().split())
people = [int(x) for x in input().split()]
tents = defaultdict(list)

for _ in range(M):
	u, v = map(int, sys.stdin.readline().split())
	tents[u].append(v)
	tents[v].append(u)

tents_list = []
for i in range(1,N+1):
    tents_list.append(i)

tent_groups = []
visited = [0]*(N+1)
tent_count = 1
while(len(tents_list)>0):
    visited[tents_list[0]] = 1
    q = [tents_list[0]]
    group = [tents_list[0]]
    tents_list.pop(0)
    while(len(q)>0):
        start = q[0]
        q.pop(0)
        for each in tents[start]:
            if visited[each] == 0:
                visited[each] = 1
                tents_list.pop(tents_list.index(each))
                group.append(each)
                q.append(each)
    tent_groups.append(group)

target_tents = [0]*len(tent_groups)
kills = 0
for n in range(len(tent_groups)):
    temp_kills = 0
    tent_groups[n].sort()
    for i in tent_groups[n]:
        if(people[i-1] > temp_kills):
            temp_kills = people[i-1]
            target_tents[n] = i
    kills += temp_kills

injuries = sum(people) - kills
print(kills, injuries)
target_tents.sort()
print(" ".join([str(x) for x in target_tents]))
print(start-t.clock())