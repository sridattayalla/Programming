class Vertex:
    def __init__(self, key):
        self.id = key

    def setPrec(self, p):
        self.pred = p


edges = {}
VertexList = {}
vertex_count = int(input())
for i in range(1, vertex_count+1):
    VertexList[i] = Vertex(i)
for i in range(1,vertex_count+1):
    edges[i] = [int(x) for x in input().split(" ")]
start = int(input())
end = int(input())

visited = []
q = []
q.append(start)
length = 0
while(len(q)>0):
    currVertex = q.pop(0)
    visited.append(currVertex)
    for each in edges[currVertex]:
        if(each not in visited):
            VertexList[each].setPrec(currVertex)
            if(each == end):
                q = []
                temp = each
                while(temp != start):
                    length += 1
                break
            elif(edges[each]):
                q.append(each)

