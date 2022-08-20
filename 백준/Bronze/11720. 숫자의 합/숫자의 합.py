import sys

n = int(sys.stdin.readline())
card = list(map(int, list(input())))
sum = 0
for i in range(n):
    sum += card[i]
print(sum)