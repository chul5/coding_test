import sys
from collections import deque

n = int(input())


def bfs(graph, queue, goal, size):
    move = [(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
    while queue:
        x, y = queue.popleft()
        if x == goal[0] and y == goal[1]:
            break
        for i in range(8):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if 0 <= nx < size and 0 <= ny < size and graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1



for _ in range(n):
    queue = deque([])
    size = int(input())
    graph = [[0] * size for _ in range(size)]
    cx, cy = map(int, sys.stdin.readline().split())
    queue.append((cx,cy))
    fx, fy = map(int, sys.stdin.readline().split())
    bfs(graph, queue, (fx, fy), size)
    print(graph[fx][fy])