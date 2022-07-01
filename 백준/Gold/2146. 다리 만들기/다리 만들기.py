import sys
from collections import deque

n = int(input())
card = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]


def _bfs(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    visit[x][y] = True
    card[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and card[nx][ny] == 1:
                q.append((nx,ny))
                visit[nx][ny] = True
                card[nx][ny] = cnt

def bfs(island_num):
    global ans
    distant = [[-1] * n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if card[i][j] == island_num:
                queue.append((i,j))
                distant[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안 쪽에서만 탐색
            if 0<=nx<n and 0<=ny<n:
                # 아직 탐색 안 했으면
                if distant[nx][ny] == -1 and card[nx][ny] == 0:
                    distant[nx][ny] = distant[x][y] + 1
                    queue.append((nx,ny))
                if card[nx][ny] != island_num and card[nx][ny] > 0:
                    ans = min(ans, distant[x][y])
                    return

ans = sys.maxsize
cnt = 0
for i in range(n):
    for j in range(n):
        if card[i][j] == 1 and not visit[i][j]:
            cnt += 1
            _bfs(i,j)

for i in range(cnt):
    bfs(i+1)

print(ans)