n = int(input())
card = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if cnt % 3 == card[i]:
       cnt += 1

print(cnt)