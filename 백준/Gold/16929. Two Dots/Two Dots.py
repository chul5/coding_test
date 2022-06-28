import sys

n, m = map(int, input().split())
# print 찍어보면 개행 들어있어서 rstrip 이용
card = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
flag = False

def dfs(start, next, color, visit, cnt):
    global flag
    a, b = next
    visit[a][b] = True
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        # 범위 안이고 같은 컬러이면서 방문하지 않았을 때
        if 0<=nx<n and 0<=ny<m and card[nx][ny] == color and visit[nx][ny] is False:
            dfs(start, (nx,ny), color, visit, cnt + 1)
        # 범위 안이고 같은 컬러이면서 방문했다면 순환구조

        # 이렇게 하면 한번 탐색하고 이전 것 방문 표시 되어서 바로 True 반환함.
        elif start == (nx, ny) and 0<=nx<n and 0<=ny<m and card[nx][ny] == color and visit[nx][ny] is True and cnt >= 2:
            flag = True
            return



dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    for j in range(m):
        visit = [[False] * m for _ in range(n)]
        dfs((i,j),(i,j), card[i][j], visit, 0)

if flag is True:
    print("Yes")
else:
    print("No")