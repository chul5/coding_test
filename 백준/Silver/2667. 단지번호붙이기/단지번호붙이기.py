from collections import deque

n = int(input())
card = []
for _ in range(n):
    temp = list(map(int, list(input())))
    card.append(temp)

num_apart = []

def bfs(graph, start):
    queue = deque([])
    queue.append(start)
    dx = [1, -1, 0 , 0]
    dy = [0,0,1,-1]
    count = 0
    graph[start[0]][start[1]] = 2
    while queue:
        count += 1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and graph[nx][ny] ==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

    num_apart.append(count)

cnt = 0
for i in range(n):
    for j in range(n):
        if card[i][j] == 1:
            cnt += 1
            bfs(card, (i, j))

print(cnt)
for i in sorted(num_apart):
    print(i)