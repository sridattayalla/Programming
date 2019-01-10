graph = {4:[5,1], 5:[4,2], 2:[1,3,6], 1:[4,2,7], 7:[1,3], 3:[2,7,6],6:[2,3]}
visited = [4]
def dfs(vertex):
    print(vertex)
    for each in graph[vertex]:
        if each not in visited:
            visited.append(each)
            dfs(each)

dfs(4)