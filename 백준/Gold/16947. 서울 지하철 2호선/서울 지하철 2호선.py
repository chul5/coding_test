import sys
from collections import deque
sys.setrecursionlimit(100000)

n = int(input())
card = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    card[a].append(b)
    card[b].append(a)


def bfs():
    queue = deque([])
    distance = [-1] * (n+1)
    for i in range(1, n+1):
        if iscircular[i]:
            distance[i] = 0
            queue.append(i)
    while queue:
        v = queue.popleft()
        for i in card[v]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[v] + 1
    distance = distance[1:]
    print(*distance)



def dfs(current, start, visit, cnt):


    visit[current] = True
    for i in card[current]:
        if not visit[i]:
            dfs(i, start, visit, cnt+1)
        elif i == start and cnt >= 2:
            iscircular[start] = True
            return

iscircular = [False] * (n+1)
for i in range(1, n+1):
    visit = [False] * (n + 1)
    dfs(i, i, visit, 0)

bfs()