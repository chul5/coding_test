import sys
from collections import deque


def bfs(graph, start, visit):
    # queue 구조 사용
    queue = deque([])
    queue.append(start)
    # 시작은 1번 group!
    visit[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                # 새로 발견된 node들은 -1번 group!
                visit[i] = -1 * visit[v]
            # 발견된 group중에서 group이 같은지 check
            elif visit[i] == visit[v]:
                return -1
    return 1


n = int(input())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    card = [[] for _ in range(a+1)]
    visit = [False] * (a+1)
    flag = 0
    for _ in range(b):
        x, y = map(int, sys.stdin.readline().split())
        card[x].append(y)
        card[y].append(x)
    for i in range(1, a+1):
        if not visit[i]:
            flag = bfs(card, i, visit)
            if flag == -1:
                print("NO")
                break;
    if flag == 1:
        print("YES")