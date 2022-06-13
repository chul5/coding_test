n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

cnt = 0

for j in coin[::-1]:
    if k >= j:
        cnt += k // j
        k -= (k // j * j)
    if k == 0:
        break

print(cnt)