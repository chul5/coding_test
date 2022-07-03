import sys

n = int(input())
card = []
for i in range(n):
    card.append(tuple(map(int, sys.stdin.readline().split())))

card.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    for j in range(len(card[i])):
        print(card[i][j], end=' ')
    print('')