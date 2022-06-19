import sys

from collections import deque

n, m, start = map(int, sys.stdin.readline().split())
card = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    card[a].append(b)
    card[b].append(a)


def dfs(graph, start):
    visit[start] = True
    print(start, end=' ')

    for i in sorted(graph[start]):
        if not visit[i]:
            dfs(graph, i)


def bfs(graph, start):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visit[i]:
                queue.append(i)
                visit[i] = True


dfs(card, start)
visit = [False] * (n + 1)
print('')
bfs(card, start)