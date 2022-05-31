import sys

N = int(input())
card = []
for i in range(N):
    a, b, c, d = map(str, sys.stdin.readline().split())
    card.append([a, int(b), int(c), int(d)])


card.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(card[i][0])