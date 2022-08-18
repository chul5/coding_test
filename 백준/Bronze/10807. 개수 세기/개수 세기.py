n = int(input())
card = list(map(int, input().split()))

num = int(input())
cnt = 0
for i in range(n):
    if num == card[i]:
        cnt += 1

print(cnt)