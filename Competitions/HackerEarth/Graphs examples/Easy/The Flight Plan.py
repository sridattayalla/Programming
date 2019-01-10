import sys
class Vertex:
    def __init__(self, key):
        self.id = key
        self.pred = None
    def setPrec(self, p):
        self.pred = p

N, M, T, C = map(int, sys.stdin.readline().split())



# for i in range(1, N+1):
#     VertexList[i] = Vertex(i)

routes = {}
for _ in range(M):
    r = [int(x) for x in input().split(" ")]
    if r[0] in routes.keys():
        routes[r[0]].append(r[1])
    else:
        routes[r[0]] = [r[1]]
    if r[1] in routes.keys():
        routes[r[1]].append(r[0])
    else:
        routes[r[1]] = [r[0]]

start, end = map(int,sys.stdin.readline().split())
VertexList = {start:Vertex(start)}

if(start!=end):
    visited = [0]*(N+1)
    backTrace = {start:[start]}
    q = []
    q.append(start)
    while(len(q)>0):
        currVertex = q.pop(0)
        routes[currVertex].sort()
        for each in routes[currVertex]:
            if(visited[each] != 1):
                visited[each] = 1
                # VertexList[each] = Vertex(each)
                # VertexList[each].setPrec(currVertex)
                if(each not in backTrace or len(backTrace[currVertex]) < len(backTrace[each])-1):
                    backTrace[each] = backTrace[currVertex] + [each]
                if(each == end):
                    q = []
                    break
                elif(routes[each]):
                    q.append(each)
else:
    backTrace = {end:[start]}

path = []
temp = end
length = 0
print(len(backTrace[end]))
print(" ".join([str(x)for x in backTrace[end]]))







