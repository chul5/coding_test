import sys
from collections import deque

def isvalid(graph, row, col, height):
    if row < 0 or row >= n:
        return False
    if col < 0 or col >= m:
        return False
    if height < 0 or height >= h:
        return False
    if graph[height][row][col] != 0:
        return False

    return True


def bfs(graph, queue):

    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while queue:
        z, x, y= queue.popleft()

        for j in range(6):
            nx = x + dx[j]
            ny = y + dy[j]
            nz = z + dz[j]
            if isvalid(graph, nx, ny, nz):
                queue.append([nz, nx, ny])
                graph[nz][nx][ny] = graph[z][x][y] + 1


m, n, h = map(int, input().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)


bfs(graph, queue)
cnt = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))
print(cnt -1)