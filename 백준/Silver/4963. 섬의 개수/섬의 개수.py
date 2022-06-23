import sys


def dfs(graph, start):
    stack = [start]
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                stack.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1


while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    card = []
    for _ in range(m):
        card.append(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in range(m):
        for j in range(n):
            if card[i][j] == 1:
                cnt += 1
                dfs(card, (i,j))

    print(cnt)