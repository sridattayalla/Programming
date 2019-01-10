import sys
N = int(input())
roads = {}
for _ in  range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a in roads :
        roads[a].append(b)
    else:
        roads[a] = [b]

    if (b in roads):
        roads[b].append(a)
    else:
        roads[b] = [a]

girls_count = int(input())
girls = []
for _ in range(girls_count):
    girls.append(int(input()))

selected_girl = girls[0]
least_path = N

def getDistance(girl, l, visited, r):
    pl = l+1
    if 1 in r[girl]:
        return pl

    else:
        for each in r[girl]:
            if each not in visited:
                visited.append(each)
                return getDistance(each, pl, visited, r)


for girl in girls:
    path_length = getDistance(girl, 0, [], roads)
    if(path_length!=None):
        if (path_length < least_path):
            least_path = path_length
            selected_girl = girl
        elif (path_length == least_path and selected_girl > girl):
            selected_girl = girl

print(selected_girl)