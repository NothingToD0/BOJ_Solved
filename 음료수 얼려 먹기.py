n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        return False
    graph[x][y] = 1
    dfs(x, y + 1)   
    dfs(x, y -1)    
    dfs(x+1 , y)    
    dfs(x-1, y)     
    return True

answer = 0
for x in range(n):
    for y in range(m):
        if dfs(x,y) is True:
            answer +=1

print(answer)