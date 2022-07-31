sum = 0
mv = 101
for _ in range(7):
    a = int(input())
    if a % 2 != 0:
        sum += a
        mv = min(mv, a)

if sum == 0:
    print(-1)
else:
    print(sum)
    print(mv)