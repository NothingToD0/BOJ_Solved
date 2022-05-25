from collections import deque
def wall_in():
    

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

n, m = map(int, input().split())
lab = [list(int, input().split()) for _in range(m)]
int wall = 0
int virus = 0
for i in range(0,n):
    for j in range(0,m):
        if lab[i][j] == 0:
            lab[i][j] = 1
            wall+=1
            if wall == 3:
                break;
        elif lab[i][j] == 2:
        virus += 1
    
        





        



