n, m = map(int, input().split())

card = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    card[a].append(b)
    card[b].append(a)

visit = [False] * n


def dfs(num, depth):
    if depth == 4:
        print(1)
        exit()
    for i in card[num]:
        if not visit[i]:
            visit[i] = True
            dfs(i, depth + 1)
            visit[i] = False

for i in range(n):
    visit[i] = True
    dfs(i, 0)

    visit[i] = False
print(0)
