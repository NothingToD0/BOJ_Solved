import copy
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
Lab = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    Lab.append(L)
dr = [-1,0,1,0] 
dc = [0,1,0,-1]
max_value = 0
virus_list = [] 
for i in range(N):
    for j in range(M):
        if Lab[i][j] == 2:
            virus_list.append([i,j])


def select_wall(start,count):
    global max_value
    if count == 3 :
        sel_Lab = copy.deepcopy(Lab)
        for num in range(len(virus_list)):
            r, c = virus_list[num]
            spread_virus(r, c, sel_Lab)
        safe_counts = sum(i.count(0) for i in sel_Lab)
        max_value = max(max_value,safe_counts)
        return True
    else :
        for i in range(start, N*M): 
            r = i // M
            c = i % M
            if Lab[r][c] == 0 : 
                Lab[r][c] = 1 
                select_wall(i,count+1) 
                Lab[r][c] = 0


def spread_virus(r,c,sel_Lab):
    if sel_Lab[r][c] == 2:
        for dir in range(4):
            n_r = r+dr[dir]
            n_c = c+dc[dir]
            if n_r >= 0 and n_c >=0 and n_r < N and n_c < M :
                if sel_Lab[n_r][n_c] == 0 :
                    sel_Lab[n_r][n_c] = 2
                    spread_virus(n_r,n_c,sel_Lab)
select_wall(0,0)
print(max_value)
