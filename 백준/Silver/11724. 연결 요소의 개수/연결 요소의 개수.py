import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
card = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    card[a].append(b)
    card[b].append(a)

visit = [False] * (n+1)


def dfs(graph, start):
    if start == n+1:
        return
    visit[start] = True
    for i in graph[start]:
        if not visit[i]:
            dfs(graph, i)


cnt = 0
for i in range(1, n+1):
    if not visit[i]:
        cnt += 1
        dfs(card, i)
print(cnt)