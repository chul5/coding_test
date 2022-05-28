import heapq


n = int(input())
gift = []
for _ in range(n):
    a = list(map(int, input().split()))
    if len(gift) == 0 and a[0] == 0:
        print(-1)
    elif a[0] == 0:
        print(-heapq.heappop(gift))
    else:
        for i in range(1, a[0] + 1):
            heapq.heappush(gift, -a[i])
