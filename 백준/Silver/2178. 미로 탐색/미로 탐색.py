import sys
from collections import deque

n, m = map(int, input().split())

card = [list(map(int, input())) for _ in range(n)]




def bfs(graph, queue):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:

        row, col = queue.popleft()
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                queue.append([nx,ny])
                graph[nx][ny] = graph[row][col] + 1

# deque에 바로 data값을 넣으면 popleft할 때 문제가 생김
queue = deque([])
queue.append([0,0])
bfs(card, queue)
print(card[n-1][m-1])