import sys
input = sys.stdin.readline

def 무브():
    for i in range(n):
        num = i
        for j in range(h):
            if a[num][j]:
                num += 1
            elif a[num-1][j]:
                num -= 1
        if i != num:
            return 0
    return 1

def 디에프에스(cnt, idx, r):
    global ans
    if cnt == r:
        if 무브():
            ans = cnt
        return
    for i in range(idx, h):
        for j in range(n-1):
            if a[j][i]:
                continue
            if j - 1 >= 0 and a[j-1][i]:
                continue
            if j + 1 < n and a[j+1][i]:
                continue
            a[j][i] = 1
            디에프에스(cnt + 1, i, r)
            a[j][i] = 0

# 여기가 메인함수임 
n, m, h = map(int, input().split())
a = [[0]*h for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    a[y-1][x-1] = 1

ans, flag = sys.maxsize, 1
for r in range(4):
    디에프에스(0, 0, r)
    if ans != sys.maxsize:
        print(ans)
        flag = 0
        break
if flag:
    print(-1)