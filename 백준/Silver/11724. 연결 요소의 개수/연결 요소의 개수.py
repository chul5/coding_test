import sys

n, m = map(int, sys.stdin.readline().split())
card = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    card[a].append(b)
    card[b].append(a)

visit = [False] * (n+1)


# def dfs(graph, start):
#     if start == n+1:
#         return
#     visit[start] = True
#     for i in graph[start]:
#         if not visit[i]:
#             dfs(graph, i)


def dfs(graph, start):
    stack = [start]
    visit[start] = True
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visit[i]:
                stack.append(i)
                visit[i] = True


cnt = 0
for i in range(1, n+1):
    if not visit[i]:
        cnt += 1
        dfs(card, i)
print(cnt)