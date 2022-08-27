n = int(input())
card = list(map(int, input().split()))
cnt = 0
for i in card:
    if i == n:
        cnt += 1
print(cnt)