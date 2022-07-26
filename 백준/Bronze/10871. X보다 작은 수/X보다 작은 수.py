n, m = map(int, input().split())
card = list(map(int, input().split()))
for i in card:
    if i < m:
        print(i, end= ' ')