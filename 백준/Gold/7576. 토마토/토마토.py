from collections import deque

n, m = map(int, input().split())
card = []
tmt = []
def isvalid(graph ,row ,col):
    if row < 0 or row >= m:
        return False
    if col < 0 or col >= n:
        return False
    if graph[row][col] != 0:
        return False
    return True


def bfs(graph, flag):
    queue = deque([])
    for i in range(len(flag)):
        row = flag[i][0]
        col = flag[i][1]
        queue.append([row, col])

    move = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y = queue.popleft()

        for j in range(4):
            nx = x + move[j][0]
            ny = y + move[j][1]
            if isvalid(graph, nx, ny):
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1



for _ in range(m):
    card.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if card[i][j] == 1:
            tmt.append([i, j])
bfs(card, tmt)
cnt = 0
for i in card:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)