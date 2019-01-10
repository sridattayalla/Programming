import sys
import time as tm
start = tm.clock()
sys.setrecursionlimit(200000)

from collections import defaultdict

f = defaultdict(list)


def dfs(i, f, visited, ans):
    visited[i] = True

    for j in f[i]:
        if (visited[j] == False):
            dfs(j, f, visited, ans)

    ans.append(i)


n, m = map(int, input().split())
l = [int(i) for i in input().split()]
kill = 0
visited = [False for i in range(0, n + 1)]
res = []
for i in range(m):
    a, b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)
z = []
for i in range(1, n + 1):
    ans = []

    if (visited[i] == False):
        dfs(i, f, visited, ans)
    if (len(ans) != 0):
        res.append(ans)

kill = 0
for i in res:
    j = list(i)
    j = sorted(j)
    x = 0
    for k in j:
        if (l[k - 1] > x):
            x = l[k - 1]
            c = k
    kill += x
    z.append(c)

z.sort()
injured = sum(l) - kill

print(kill, injured)
print(" ".join([str(i) for i in z]))
print(tm.clock()-start)