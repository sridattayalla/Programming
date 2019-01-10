import sys
from itertools import permutations

tc = int(input())


def maxDiff(t,l):
    start = 0
    q = [start]
    max = 0
    visited = [start]
    while(len(q)>0):
        curr = q[0]
        q.pop(0)
        for each in t[curr]:
            temp = abs(l[curr]-l[each])
            if(temp>max):
                max = temp
            if(each not in visited):
                visited.append(each)
                q.append(each)
    return max

def arrange(l, t, parent_tree, pos):
    ret_list = []
    if(len(l) == 0):
        return [maxDiff(parent_tree, t)]
    else:
        for i in range(len(l)):
            t[pos] = l[i]
            temp_l = l[:]
            del temp_l[i]
            ret_list = ret_list + arrange(temp_l, t, parent_tree, pos+1)
    return ret_list

for _ in range(tc):
    N = int(input())
    values = [int(x) for x in input().split(" ")]
    tree = {}
    for _ in range(N-1):
        temp_u, temp_v = map(int, sys.stdin.readline().split())
        u = temp_u-1
        v = temp_v-1

        if u not in tree:
            tree[u] = [v]
        else:
            tree[u].append(v)
        if v not in tree:
            tree[v] = [u]
        else:
            tree[v].append(u)
    perm = permutations(values)
    min = maxDiff(tree, values)
    for each in list(perm):
        temp = maxDiff(tree, list(each))
        if min>temp:
            min = temp
    print(min)
    # l = arrange(values, [0]*len(values), tree, 0)
    # sorted(l)
    # print(l[0])
